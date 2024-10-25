from math import sqrt

print("This is a diagnostic algorithm. Please answer the following questions for your diagnosis.")

#Initial
temp = float(input("Enter your temperature (°C): "))
temp_location = str(input("Was the temperature measured Orally (O) or Underarm (U)? (enter O or U): "))

#Functions
def flu_or_infection() -> None:
    """
    Diagnose flu or infection based on the nausea input.
    """
    nausea = str(input(f"\nAre you experienceing nausea? (y or n): "))
    if nausea.lower() == "y":
        print(f"\nDiagnosis: Flu")
    elif nausea.lower() == "n":
        print(f"\nDiagnosis: infection")
    else:
        print("\033[1mERROR:\033[0m Invalid Entry. Please Enter \"y\" or \"n\"")
        flu_or_infection()


def stress_or_healthy() -> None:
    """
    Disagnose stress or healthy based on an HRV calculation that thakes threee user inputs.
    """
    print(f"\nPlease enter 3 heartbeat intervals in ms...")
    interval_a = float(input("Enter first interval: "))
    interval_b = float(input("Enter second interval: "))
    interval_c = float(input("Enter third interval: "))

    HRV = sqrt(((interval_a - interval_b)**2 + (interval_b - interval_c)**2)/2)

    if HRV < 50:
        cortisol = float(input("Enter cortisol level in mgc/dL: "))
        if cortisol > 25:
            print(f"\nDiagnosis: Stress")
        else:
            print(f"\nDiagnosis: Healthy")
    else:
        print(f"\nDiagnosis: Healthy")


#Main Loop
def main() -> None:
    if temp >= 37.8 and temp_location.upper() == "O" or temp >= 37.2 and temp_location.upper() == "U":
        flu_or_infection()
    else:
        stress_or_healthy()

main()
