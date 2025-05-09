def function(x):
    return x ** 2

def derivative(x):
    return 2 * x

def perform_gradient_descent(starting_point, step_size, iterations):

    current_x = starting_point

    print(f"{'Step':<10}{'x':<10.2}{'y = f(x)':<10}")
    for step in range(iterations):

        gradient = derivative(current_x)
        current_x = current_x - step_size * gradient
        print(f"{step+1:<10}{current_x:<10.2f}{function(current_x):<10.2f}")

    return current_x

start_x = 99
alpha = 0.2
steps = 10

result_x = perform_gradient_descent(start_x, alpha, steps)
print(f"\nFunction reaches minimum at x = {result_x:.2f}")

