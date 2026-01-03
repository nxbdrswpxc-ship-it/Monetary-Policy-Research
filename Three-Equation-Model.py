A = 1.0          # autonomous demand
a = 0.5          # interest sensitivity
alpha = 0.4      # Phillips curve slope
beta = 1.0       # CB inflation weight

y_e = 1.0        # equilibrium (potential) output
pi_0 = 0.04      # last period inflation (4%)
pi_T = 0.02      # inflation target (2%)

def IS_curve(r):
    """IS curve: output next period"""
    return A - a * r

def phillips_curve(y):
    """Phillips curve: inflation next period"""
    return pi_0 + alpha * (y - y_e)

def loss_function(r):
    """Central bank loss function"""
    y = IS_curve(r)
    pi = phillips_curve(y)
    loss = (y - y_e)**2 + beta * (pi - pi_T)**2
    return loss

def optimal_interest_rate():
    """
    Closed-form optimal r*
    Derived from dL/dr = 0
    """
    numerator = a * (A - y_e) + beta * alpha * a * (pi_0 - pi_T)
    denominator = a**2 + beta * (alpha * a)**2
    return numerator / denominator

def run_model():
    r_user = float(input("Enter real interest rate (e.g. 0.05 for 5%): "))

    y_user = IS_curve(r_user)
    pi_user = phillips_curve(y_user)
    loss_user = loss_function(r_user)

    r_star = optimal_interest_rate()
    y_star = IS_curve(r_star)
    pi_star = phillips_curve(y_star)
    loss_star = loss_function(r_star)

    print("\n--- Your policy ---")
    print(f"Output next quarter: {y_user:.3f}")
    print(f"Inflation next quarter: {pi_user:.2%}")
    print(f"Loss: {loss_user:.4f}")

    print("\n--- Optimal policy ---")
    print(f"Optimal interest rate: {r_star:.2%}")
    print(f"Output: {y_star:.3f}")
    print(f"Inflation: {pi_star:.2%}")
    print(f"Loss: {loss_star:.4f}")

run_model()