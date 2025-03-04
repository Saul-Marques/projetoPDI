import os
import logging
from django.conf import settings
from django.shortcuts import render, redirect
from loja.models import Product, Categoria, ProductImage
from decimal import Decimal
from loja.forms import ProductForm

logger = logging.getLogger(__name__)  # Logger para debug

def upload_product_view(request):
    if "user_id" not in request.session:
        return redirect("login")

    if request.method == "POST":
        nome = request.POST.get("nome")
        preco = request.POST.get("preco").replace(",", ".")
        descricao = request.POST.get("descricao")
        categoria_id = request.POST.get("categoria")
        images = request.FILES.getlist("images")  # Obtém todas as imagens enviadas

        try:
            preco = Decimal(preco)
        except ValueError:
            return render(request, "upload_product.html", {
                "categorias": Categoria.objects.all(),
                "error": "O preço inserido é inválido. Use números com até duas casas decimais."
            })

        categoria = Categoria.objects.get(id=categoria_id)
        product = Product(
            nome=nome,
            preco=preco,
            descricao=descricao,
            categoria=categoria,
            user_id=request.session["user_id"]
        )
        product.save()

        # Criar a pasta do produto se não existir
        product_folder = os.path.join(settings.MEDIA_ROOT, "uploads", "products", str(product.id))
        os.makedirs(product_folder, exist_ok=True)

        # Verificar se imagens foram enviadas
        if not images:
            logger.warning(f"⚠ Nenhuma imagem foi enviada para o produto {product.id}")

        # Guardar as imagens dentro da pasta correta
        for image in images:
            image_name = image.name.replace(" ", "_")  # Evita espaços nos nomes dos arquivos
            image_path = os.path.join(product_folder, image_name)  # Caminho absoluto
            relative_image_path = f"uploads/products/{product.id}/{image_name}"  # Caminho relativo

            try:
                # Gravar a imagem no sistema de arquivos
                with open(image_path, "wb+") as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)

                product_image = ProductImage.objects.create(product=product, image=relative_image_path)

            except Exception as e:
                logger.error(f" Erro ao guardar imagem {image_name}: {e}")

        return redirect("homepage")

    categorias = Categoria.objects.all()
    return render(request, "upload_product.html", {"categorias": categorias})
