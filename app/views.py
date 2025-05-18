from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import View

from .forms import PostForm
from .models import Category, Combo, Kind, Status, SubCategory, Transaction


class HomeView(View):
    def get(self, request):
        transactions = Transaction.objects.select_related(
            "status", "combo__kind", "combo__category", "combo__sub_category"
        )
        # получаем что-то для фильтрации
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        status = request.GET.get("status")
        kind = request.GET.get("kind")
        category = request.GET.get("category")
        sub_category = request.GET.get("sub_category")
        if status:
            transactions = transactions.filter(status__name=status)
        if start_date:
            transactions = transactions.filter(created_at__gte=start_date)
        if end_date:
            transactions = transactions.filter(created_at__lte=end_date)
        if kind:
            transactions = transactions.filter(combo__kind__name=kind)
        if category:
            transactions = transactions.filter(combo__category__name=category)
        if sub_category:
            transactions = transactions.filter(combo__sub_category__name=sub_category)

        result = table(transactions)

        statuses = Status.objects.all()
        kinds = Kind.objects.all()
        categories = Category.objects.all()
        sub_categories = SubCategory.objects.all()
        return render(
            request,
            "app/index.html",
            {
                "result": result,
                "statuses": statuses,
                "kinds": kinds,
                "categories": categories,
                "sub_categories": sub_categories,
            },
        )


def form(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            status_name = form.cleaned_data["status"]
            kind_name = form.cleaned_data["kind"]
            category_name = form.cleaned_data["category"]
            sub_category_name = form.cleaned_data["sub_category"]
            amount = form.cleaned_data["amount"]
            note = form.cleaned_data["note"]

            # Получаем или создаём объекты по имени
            status_obj, _ = Status.objects.get_or_create(name=status_name)
            kind_obj, _ = Kind.objects.get_or_create(name=kind_name)
            category_obj, _ = Category.objects.get_or_create(name=category_name)
            sub_category_obj, _ = SubCategory.objects.get_or_create(
                name=sub_category_name
            )

            # Ищем или создаём Combo
            combo_obj, _ = Combo.objects.get_or_create(
                kind=kind_obj, category=category_obj, sub_category=sub_category_obj
            )

            # Создаём транзакцию
            Transaction.objects.create(
                created_at=timezone.now(),
                status=status_obj,
                combo=combo_obj,
                amount=amount,
                note=note,
            )
        return redirect("form")
    else:
        form = PostForm()

    transactions = Transaction.objects.select_related(
        "status", "combo__kind", "combo__category", "combo__sub_category"
    )
    result = table(transactions)
    return render(request, "app/post_edit.html", {"form": form, "result": result})


def get_categories(request):
    kind_name = request.GET.get("kind_id")
    combos = Combo.objects.filter(kind__name=kind_name)
    categories = {c.category.name for c in combos}
    return JsonResponse({"categories": list(categories)})


def get_subcategories(request):
    category_name = request.GET.get("category_id")
    combos = Combo.objects.filter(category__name=category_name)
    sub_categories = {c.sub_category.name for c in combos}
    return JsonResponse({"sub_categories": list(sub_categories)})


def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            status_obj, _ = Status.objects.get_or_create(
                name=form.cleaned_data["status"]
            )
            kind_obj, _ = Kind.objects.get_or_create(name=form.cleaned_data["kind"])
            category_obj, _ = Category.objects.get_or_create(
                name=form.cleaned_data["category"]
            )
            sub_category_obj, _ = SubCategory.objects.get_or_create(
                name=form.cleaned_data["sub_category"]
            )
            combo_obj, _ = Combo.objects.get_or_create(
                kind=kind_obj, category=category_obj, sub_category=sub_category_obj
            )

            transaction.status = status_obj
            transaction.combo = combo_obj
            transaction.amount = form.cleaned_data["amount"]
            transaction.note = form.cleaned_data["note"]
            transaction.save()
            return redirect("form")
    else:
        form = PostForm(
            initial={
                "status": transaction.status.name if transaction.status else "",
                "kind": transaction.combo.kind.name,
                "category": transaction.combo.category.name,
                "sub_category": transaction.combo.sub_category.name,
                "amount": transaction.amount,
                "note": transaction.note,
            }
        )

    return render(
        request, "app/edit_transaction.html", {"form": form, "transaction": transaction}
    )


def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect("form")


def table(transactions):
    result = []
    for t in transactions:
        result.append(
            {
                "id": t.id,
                "created_at": t.created_at,
                "status": t.status.name if t.status else None,
                "kind": t.combo.kind.name,
                "category": t.combo.category.name,
                "sub_category": t.combo.sub_category.name,
                "amount": t.amount,
                "note": t.note,
            }
        )
    return result
