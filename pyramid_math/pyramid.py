from .geometry import (
    calculate_apothem,
    calculate_edge,
    calculate_slope_angle,
    calculate_diagonal,
    np
)
import math
from .constants import PHI, PI
from .database import PYRAMID_DATABASE

class Pyramid:
    def __init__(self, name, base_length_north, base_length_east, height):
        self.name = name
        self.base_length_north = base_length_north
        self.base_length_east = base_length_east
        self.height = height

    @classmethod
    def from_database(cls, pyramid_id):
        if pyramid_id not in PYRAMID_DATABASE:
            raise KeyError(f"Pyramid '{pyramid_id}' not found in database")
        data = PYRAMID_DATABASE[pyramid_id]
        return cls(
            name=data["name"],
            base_length_north=data["base_length_north"],
            base_length_east=data["base_length_east"],
            height=data["height"]
        )

    def pi_ratio(self):
        return round(self.base_length_north / self.height, 4)

    # Method to calculate golden ratio (approximate)
    def golden_ratio(self):
        return round(self.base_length_north / self.height, 4)

    # Static method to compare two pyramids by name
    @staticmethod
    def compare_pyramids(pyramid1_name, pyramid2_name):
        # Fetch pyramid data from database
        pyramid1 = PYRAMID_DATABASE.get(pyramid1_name)
        pyramid2 = PYRAMID_DATABASE.get(pyramid2_name)

        if not pyramid1 or not pyramid2:
            raise ValueError("One or both pyramid names are invalid.")
        
        # Create Pyramid objects for each pyramid name
        p1 = Pyramid(pyramid1["name"], pyramid1["base_length_north"], pyramid1["base_length_east"], pyramid1["height"])
        p2 = Pyramid(pyramid2["name"], pyramid2["base_length_north"], pyramid2["base_length_east"], pyramid2["height"])

        # Compare their properties and create a comparison dictionary
        comparison = {
            p1.name: {
                'height': p1.height,
                'base_length': p1.base_length_north,
                'slope_angle': calculate_slope_angle(p1.base_length_north, p1.height),
                'pi_ratio': p1.pi_ratio(),
                'golden_ratio': p1.golden_ratio()
            },
            p2.name: {
                'height': p2.height,
                'base_length': p2.base_length_north,
                'slope_angle': calculate_slope_angle(p2.base_length_north, p2.height),
                'pi_ratio': p2.pi_ratio(),
                'golden_ratio': p2.golden_ratio()
            }
        }

        return comparison
    def perform_special_calculations(self):
        pivalue = (self.base_length_north + self.base_length_east) / self.height
        goldenratio = calculate_edge(self.base_length_north, self.height) / (self.base_length_north / 2)
        sqrt_goldenratio = calculate_apothem(self.base_length_east,self.height) / self.height
        slope_angle = calculate_slope_angle(self.base_length_north, self.height)
        return {
            'pivalue': pivalue,
            'goldenratio': goldenratio,
            'sqrt_goldenratio': sqrt_goldenratio,
            'difference_from_pi': abs(pivalue - PI),
            'difference_from_phi': abs(goldenratio - PHI),
            'slope_angle': slope_angle
            
        }

    def calculate_tribonacci_constant(self):
        """
        Calculate the Tribonacci constant using the formula:
        (CG + CG + Half Base Length) / (Slant Length + Base Length)
        """
        cg = calculate_diagonal(self.base_length_north)
        half_base = self.base_length_north / 2
        slant_length = calculate_apothem(self.base_length_north, self.height)  # Using apothem as slant length

        tribonacci_constant = (cg + cg + half_base) / (slant_length + self.base_length_north)
        return tribonacci_constant

    def compare_tribonacci_constant(self):
        """
        Compare the calculated Tribonacci constant to the known Tribonacci constant
        """
        tribonacci_constant = self.calculate_tribonacci_constant()
        # Actual Tribonacci constant
        tribonacci_actual = 1.839286755
        difference = abs(tribonacci_constant - tribonacci_actual)
        return tribonacci_constant, difference

    def compare_root_5(self):
        """
        Compare (Base Length + Apothem) / Apothem to √5
        """
        apothem = calculate_apothem(self.base_length_north, self.height)
        root_5 = np.sqrt(5)
        ratio = (self.base_length_north + apothem) / apothem
        difference = abs(ratio - root_5)
        return ratio, difference

    def compare_root_3(self):
        """
        Compare (Height + CG + CG) / (North Base + Eastern Base) to √3
        """
        cg = calculate_diagonal(self.base_length_north)
        root_3 = np.sqrt(3)
        ratio = (self.height + cg + cg) / (self.base_length_north + self.base_length_east)
        difference = abs(ratio - root_3)
        return ratio, difference

    def compare_golden_ratio_minus_1(self):
        """
        Compare (Apothem / (Apothem + Half Base Length)) to φ - 1
        """
        apothem = calculate_apothem(self.base_length_north, self.height)
        half_base = self.base_length_north / 2
        golden_ratio = (1 + np.sqrt(5)) / 2
        ratio = apothem / (apothem + half_base)
        difference = abs(ratio - (golden_ratio - 1))
        return ratio, difference
    
    def compare_CG_base_length(self):
        """
        Compare CG to Base length and check the difference with √2
        """
        cg = calculate_diagonal(self.base_length_north)
        ratio = cg / self.base_length_north
        sqrt_2 = np.sqrt(2)
        difference = abs(ratio - sqrt_2)
        return ratio, difference

    def detailed_analysis(self):
        """
        Comprehensive analysis of the pyramid with constant comparisons
        """
        # Perform special calculations
        special_calcs = self.perform_special_calculations()

        print(f"Detailed Analysis of {self.name}:")
        print("\nMeasurements and Calculated Values:")
        print(f"North Base Length: {self.base_length_north:.2f} ft")
        print(f"Eastern Base Length: {self.base_length_east:.2f} ft")
        print(f"Height: {self.height:.2f} ft")

        print("\nSpecial Calculations vs Mathematical Constants:")
        
        # Pi Value Comparison
        print(f"(North base + Eastern base) / Height = {special_calcs['pivalue']:.4f}")
        print(f"Actual π value = {math.pi:.4f}")
        print(f"Difference from π = {abs(special_calcs['pivalue'] - math.pi):.4f}")

        # Golden Ratio Comparison
        print(f"Edge / (Base length / 2) = {special_calcs['goldenratio']:.4f}")
        phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        print(f"Actual φ (Golden Ratio) = {phi:.4f}")
        print(f"Difference from φ = {abs(special_calcs['goldenratio'] - phi):.4f}")

        # Square Root of Golden Ratio Comparison
        print(f"Apothem / Height = {special_calcs['sqrt_goldenratio']:.4f}")
        sqrt_phi = np.sqrt(phi)
        print(f"Actual √φ = {sqrt_phi:.4f}")
        print(f"Difference from √φ = {abs(special_calcs['sqrt_goldenratio'] - sqrt_phi):.4f}")

        # Slope Angle
        print(f"\nPyramid Slope Angle: {special_calcs['slope_angle']:.2f} degrees")

        # CG and Base Length Comparison
        cg_ratio, cg_difference = self.compare_CG_base_length()
        print(f"calculate_diagonal  (CG) / Base Length = {cg_ratio:.4f}")
        print(f"Difference from √2 = {cg_difference:.4f}")

        # Tribonacci Constant Calculation and Comparison
        tribonacci_constant, tribonacci_difference = self.compare_tribonacci_constant()
        print(f"\nCalculated Tribonacci Constant = {tribonacci_constant:.4f}")
        print(f"Actual Tribonacci Constant = 1.8393")
        print(f"Difference from Tribonacci Constant = {tribonacci_difference:.4f}")

        # Root 5 Calculation and Comparison
        root_5_ratio, root_5_difference = self.compare_root_5()
        print(f"\n(Base Length + Apothem) / Apothem = {root_5_ratio:.4f}")
        print(f"Actual √5 = {np.sqrt(5):.4f}")
        print(f"Difference from √5 = {root_5_difference:.4f}")

        # Root 3 Calculation and Comparison
        root_3_ratio, root_3_difference = self.compare_root_3()
        print(f"\n(Height + CG + CG) / (North Base + Eastern Base) = {root_3_ratio:.4f}")
        print(f"Actual √3 = {np.sqrt(3):.4f}")
        print(f"Difference from √3 = {root_3_difference:.4f}")

        # Golden Ratio - 1 Comparison
        golden_ratio_minus_1_ratio, golden_ratio_minus_1_difference = self.compare_golden_ratio_minus_1()
        print(f"\nApothem / (Apothem + Half Base Length) = {golden_ratio_minus_1_ratio:.4f}")
        print(f"Actual φ - 1 = {phi - 1:.4f}")
        print(f"Difference from φ - 1 = {golden_ratio_minus_1_difference:.4f}")

    @staticmethod
    def list_pyramids():
        return {pid: data["name"] for pid, data in PYRAMID_DATABASE.items()}
