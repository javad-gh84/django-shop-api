## Django REST

Install the project dependencies with:

```powershell
python -m pip install -r requirements.txt
```

The product read API exposes:

- `GET /api/products/` — list products.
- `GET /api/products/<id>/` — retrieve one product.

Both endpoints use `ProductSerializer`. Each product also includes `final_price`,
which returns its discounted price when one is set, or its regular price otherwise.
