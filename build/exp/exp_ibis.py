import ibis

xy = ibis.schema({"x": int, "y": str})
xy2 = ibis.schema({"x": int, "y": str})
yx = ibis.schema({"y": str, "x": int})
xy_float = ibis.schema({"x": float, "y": str})