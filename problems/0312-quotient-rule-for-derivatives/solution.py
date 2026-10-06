import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:

    if len(g_coeffs) == 3 and len(h_coeffs) == 2:
        g = (g_coeffs[0]*(x**2)) + (g_coeffs[1]*x) + g_coeffs[2]
        h = (h_coeffs[0]*x) + h_coeffs[1]
        g_der = ((g_coeffs[0]*(2*x))) + (g_coeffs[1])
        h_der = (h_coeffs[0])
    elif len(g_coeffs) == 3 and len(h_coeffs) == 3:
        g = (g_coeffs[0]*(x**2)) + (g_coeffs[1]*x) + g_coeffs[2]
        h = (h_coeffs[0]*(x**2)) + (h_coeffs[1]*x) + h_coeffs[2]
        g_der = ((g_coeffs[0]*(2*x))) + (g_coeffs[1])
        h_der = ((h_coeffs[0]*(2*x))) + (h_coeffs[1])
    elif len(g_coeffs) == 2 and len(h_coeffs) == 3:
        g = (g_coeffs[0]*x) + g_coeffs[1]
        h = (h_coeffs[0]*(x**2)) + (h_coeffs[1]*x) + h_coeffs[2]
        g_der = (g_coeffs[0])
        h_der = ((h_coeffs[0]*(2*x))) + (h_coeffs[1])
    elif len(g_coeffs) == 1 and len(h_coeffs) == 2:
        g = g_coeffs[0]
        h = (h_coeffs[0]*x) + h_coeffs[1]
        g_der = 0
        h_der = h_coeffs[0]
    
    result = ((g_der*h) - (g*h_der)) / h**2
    
    return result
    pass