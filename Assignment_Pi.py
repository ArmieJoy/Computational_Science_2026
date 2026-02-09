#=============Area of an Ellipse with Pi Precision Analysis=============

from decimal import Decimal, getcontext

# Ellipse area function
def ellipse_area(a, b, pi_value):
    return pi_value * Decimal(a) * Decimal(b)

# Semi-major and semi-minor axes
a, b = 5, 3

# Precomputed string of pi with 100+ digits
pi_str = (
    "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
)

# -------------------- ROUNDED SECTION --------------------
def round_pi(n):
    getcontext().prec = n + 10   # extra precision margin
    pi_val = Decimal(pi_str)
    return pi_val.quantize(Decimal('1.' + '0'*n))  # round to n decimals

pi_precisions_rounded = {
    "4 decimals": round_pi(4),
    "20 decimals": round_pi(20),
    "40 decimals": round_pi(40),
    "60 decimals": round_pi(60),
    "100 decimals": round_pi(100)
}

areas_rounded = {label: ellipse_area(a, b, pi_val) for label, pi_val in pi_precisions_rounded.items()}

print(f"Semi-major axis = {a}, Semi-minor axis = {b}\n")
print("=== Rounded Results ===")
for label, area in areas_rounded.items():
    # format to 20 decimals consistently
    print(f"Using {label} of pi (rounded): Area = {area.normalize()}")

print("\nDifferences between rounded precisions:")
labels = list(areas_rounded.keys())
for i in range(len(labels) - 1):
    diff = abs(areas_rounded[labels[i]] - areas_rounded[labels[i+1]])
    print(f"Gap between {labels[i]} and {labels[i+1]}: {diff.normalize()}")

# -------------------- TRUNCATED SECTION --------------------
def truncate_pi(n):
    getcontext().prec = n + 10   # extra precision margin
    cutoff = pi_str.find('.') + n + 1
    return Decimal(pi_str[:cutoff])

pi_precisions_truncated = {
    "4 decimals": truncate_pi(4),
    "20 decimals": truncate_pi(20),
    "40 decimals": truncate_pi(40),
    "60 decimals": truncate_pi(60),
    "100 decimals": truncate_pi(100)
}

areas_truncated = {label: ellipse_area(a, b, pi_val) for label, pi_val in pi_precisions_truncated.items()}

print("\n=== Truncated Results ===")
for label, area in areas_truncated.items():
    # normalize to remove trailing zeros
    print(f"Using {label} of pi (truncated): Area = {area.normalize()}")

print("\nDifferences between truncated precisions:")
labels = list(areas_truncated.keys())
for i in range(len(labels) - 1):
    diff = abs(areas_truncated[labels[i]] - areas_truncated[labels[i+1]])
    print(f"Gap between {labels[i]} and {labels[i+1]}: {diff.normalize()}")

#============================================================================

print("\nDifferences between rounded and truncated precisions:")
labels = list(areas_truncated.keys())
for i in range(len(labels) - 1):
    diff = abs(areas_rounded[labels[i]] - areas_truncated[labels[i]])
    print(f"Gap between rounded {labels[i]} and truncated {labels[i]}: {diff.normalize()}")

#===============================================================================with graphics
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt

# Ellipse area function
def ellipse_area(a, b, pi_value):
    return pi_value * Decimal(a) * Decimal(b)

# Semi-major and semi-minor axes
a, b = 5, 3

# Precomputed string of pi with 100+ digits
pi_str = (
    "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
)

# -------------------- ROUNDED SECTION --------------------
def round_pi(n):
    getcontext().prec = n + 10   # extra precision margin
    pi_val = Decimal(pi_str)
    return pi_val.quantize(Decimal('1.' + '0'*n))  # round to n decimals

pi_precisions_rounded = {
    4: round_pi(4),
    20: round_pi(20),
    40: round_pi(40),
    60: round_pi(60),
    100: round_pi(100)
}

areas_rounded = {n: ellipse_area(a, b, pi_val) for n, pi_val in pi_precisions_rounded.items()}

# -------------------- TRUNCATED SECTION --------------------
def truncate_pi(n):
    getcontext().prec = n + 10   # extra precision margin
    cutoff = pi_str.find('.') + n + 1
    return Decimal(pi_str[:cutoff])

pi_precisions_truncated = {
    4: truncate_pi(4),
    20: truncate_pi(20),
    40: truncate_pi(40),
    60: truncate_pi(60),
    100: truncate_pi(100)
}

areas_truncated = {n: ellipse_area(a, b, pi_val) for n, pi_val in pi_precisions_truncated.items()}

# -------------------- GRAPHICS SECTION --------------------
plt.figure(figsize=(10,6))

# Plot rounded results
plt.plot(list(areas_rounded.keys()), [float(v) for v in areas_rounded.values()],
         marker='o', label="Rounded π")

# Plot truncated results
plt.plot(list(areas_truncated.keys()), [float(v) for v in areas_truncated.values()],
         marker='s', label="Truncated π")

plt.title("Ellipse Area vs π Precision")
plt.xlabel("Decimal Places of π")
plt.ylabel("Ellipse Area (a=5, b=3)")
plt.legend()
plt.grid(True)
plt.show()

#=============================================================================
#=============================================================================

#============Formula with Pi Precision Analysis=============

from decimal import Decimal, getcontext

def formula(pi_value):
    return Decimal(1) / (pi_value * Decimal(2)).sqrt()

# Define radius
# radius = 8

# Precomputed string of pi with 100+ digits
pi_str = (
    "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
)

# -------------------- ROUNDED SECTION --------------------
def round_pi(n):
    getcontext().prec = n + 10   # extra precision margin
    pi_val = Decimal(pi_str)
    return pi_val.quantize(Decimal('1.' + '0'*n))  # round to n decimals

pi_precisions_rounded = {
    "4 decimals": round_pi(4),
    "20 decimals": round_pi(20),
    "40 decimals": round_pi(40),
    "60 decimals": round_pi(60),
    "100 decimals": round_pi(100)
}

formula_rounded = {label: formula( pi_val) for label, pi_val in pi_precisions_rounded.items()}

# print(f"Radius = {radius}\n")
print("=== Rounded Results ===")
for label, answer in formula_rounded.items():
    # format to 20 decimals consistently
    print(f"Using {label} of pi (rounded): Answer = {answer.normalize()}")

print("\nDifferences between rounded precisions:")
labels = list(formula_rounded.keys())
for i in range(len(labels) - 1):
    diff = abs(formula_rounded[labels[i]] - formula_rounded[labels[i+1]])
    print(f"Gap between {labels[i]} and {labels[i+1]}: {diff.normalize()}")

# -------------------- TRUNCATED SECTION --------------------
def truncate_pi(n):
    getcontext().prec = n + 10   # extra precision margin
    cutoff = pi_str.find('.') + n + 1
    return Decimal(pi_str[:cutoff])

pi_precisions_truncated = {
    "4 decimals": truncate_pi(4),
    "20 decimals": truncate_pi(20),
    "40 decimals": truncate_pi(40),
    "60 decimals": truncate_pi(60),
    "100 decimals": truncate_pi(100)
}

formula_truncated = {label: formula( pi_val) for label, pi_val in pi_precisions_truncated.items()}

print("\n=== Truncated Results ===")
for label, answer in formula_truncated.items():
    # normalize to remove trailing zeros
    print(f"Using {label} of pi (truncated): Answer = {answer.normalize()}")

print("\nDifferences between truncated precisions:")
labels = list(formula_truncated.keys())
for i in range(len(labels) - 1):
    diff = abs(formula_truncated[labels[i]] - formula_truncated[labels[i+1]])
    print(f"Gap between {labels[i]} and {labels[i+1]}: {diff.normalize()}")

#=============================================================================

print("\nDifferences between rounded and truncated precisions:")
labels = list(formula_truncated.keys())
for i in range(len(labels) - 1):
    diff = abs(formula_rounded[labels[i]] - formula_truncated[labels[i+1]])
    print(f"Gap between {labels[i]} and {labels[i+1]}: {diff.normalize()}")

#============================================================================
#============================================================================

#=========Volume of a Sphere with Pi Precision Analysis=========

from decimal import Decimal, getcontext

# Sphere volume function (using Decimal consistently)
def sphere_volume(radius, pi_value):
    return (Decimal(4) / Decimal(3)) * pi_value * (Decimal(radius) ** 3)

# Define radius
radius = 5

# Precomputed string of pi with 100+ digits
pi_str = (
    "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
)

# -------------------- ROUNDED SECTION --------------------
def round_pi(n):
    getcontext().prec = n + 10   # extra precision margin
    pi_val = Decimal(pi_str)
    return pi_val.quantize(Decimal('1.' + '0'*n))  # round to n decimals

pi_precisions_rounded = {
    "4 decimals": round_pi(4),
    "20 decimals": round_pi(20),
    "40 decimals": round_pi(40),
    "60 decimals": round_pi(60),
    "100 decimals": round_pi(100)
}

volumes_rounded = {label: sphere_volume(radius, pi_val) for label, pi_val in pi_precisions_rounded.items()}

print(f"Radius = {radius}\n")
print("=== Rounded Results ===")
for label, volume in volumes_rounded.items():
    print(f"Using {label} of pi (rounded): Volume = {volume.normalize()}")

print("\nDifferences between rounded precisions:")
labels = list(volumes_rounded.keys())
for i in range(len(labels) - 1):
    diff = abs(volumes_rounded[labels[i]] - volumes_rounded[labels[i+1]])
    print(f"Gap between {labels[i]} and {labels[i+1]}: {diff.normalize()}")

# -------------------- TRUNCATED SECTION --------------------
def truncate_pi(n):
    getcontext().prec = n + 10   # extra precision margin
    cutoff = pi_str.find('.') + n + 1
    return Decimal(pi_str[:cutoff])

pi_precisions_truncated = {
    "4 decimals": truncate_pi(4),
    "20 decimals": truncate_pi(20),
    "40 decimals": truncate_pi(40),
    "60 decimals": truncate_pi(60),
    "100 decimals": truncate_pi(100)
}

volumes_truncated = {label: sphere_volume(radius, pi_val) for label, pi_val in pi_precisions_truncated.items()}

print("\n=== Truncated Results ===")
for label, volume in volumes_truncated.items():
    # normalize to remove trailing zeros
    print(f"Using {label} of pi (truncated): Volume = {volume.normalize()}")

print("\nDifferences between truncated precisions:")
labels = list(volumes_truncated.keys())
for i in range(len(labels) - 1):
    diff = abs(volumes_truncated[labels[i]] - volumes_truncated[labels[i+1]])
    print(f"Gap between {labels[i]} and {labels[i+1]}: {diff.normalize()}")

#============================================================================

print("\nDifferences between rounded and truncated precisions:")
labels = list(volumes_truncated.keys())
for i in range(len(labels) - 1):
    diff = abs(volumes_rounded[labels[i]] - volumes_truncated[labels[i]])
    print(f"Gap between {labels[i]} and {labels[i+1]}: {diff.normalize()}")

# #============================================================================
# #============================================================================