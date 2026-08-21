import ibis

# Cleans FAME's coordinate strings and returns a Float64.
def convert_dms_to_decimal(coord_expr: ibis.expr.types.StringScalar) -> ibis.expr.types.Floating64Scalar:
   
    if coord_expr is None:
        return ibis.literal(None, type="float64")
    
    # Extracts the 4 critical groups: Degrees, Minutes, Seconds, and Direction
    pattern = r"(\d+)[^\d]+(\d+)[^\d]+([\d\.]+)[^\d]+([NSEW])"
    
    deg         = coord_expr.re_extract(pattern, 1).cast("float64")
    min         = coord_expr.re_extract(pattern, 2).cast("float64")
    sec         = coord_expr.re_extract(pattern, 3).cast("float64")
    direction   = coord_expr.re_extract(pattern, 4)
    
    decimal = deg + (min / 60.0) + (sec / 3600.0)
    
    # South and West must be mathematically negative
    return ibis.cases(
        (direction.isin(["S", "W"]), -decimal),
        else_=decimal
    )

def test_convert_dms_to_decimal():
    test_cases = [
        ("51°30'26.0\"N", 51.507222),
        ("0°7'39.0\"W", -0.1275),
        ("40°42'46.0\"N", 40.712778),
        ("74°0'21.0\"W", -74.005833),
        ("34°3'8.0\"S", -34.052222),
        ("118°14'37.0\"E", 118.243611),
        ("51Â° 39' 35.8\" N", 51.659944),
        ("51Â° 25' 50.9\" N", 51.430806),
        ("0Â° 7' 39.0\" W", -0.1275),
        ("0Â° 7' 39.0\" E", 0.1275),
    ]
    
    for dms, expected in test_cases:
        result = convert_dms_to_decimal(ibis.literal(dms)).execute()
        assert abs(result - expected) < 1e-6, f"Test failed for {dms}. Expected: {expected}, Got: {result}"
    
    print("✅ All tests passed for convert_dms_to_decimal function.")

if __name__ == "__main__":
    test_convert_dms_to_decimal()