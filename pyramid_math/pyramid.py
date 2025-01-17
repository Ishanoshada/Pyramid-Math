from .geometry import (
    calculate_apothem,
    calculate_edge,
    calculate_slope_angle,
    calculate_diagonal,
    np
)
import math,json
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
        return round(self.base_length_north / self.height, 9)

    # Method to calculate golden ratio (approximate)
    def golden_ratio(self):
        return round(self.base_length_north / self.height, 9)

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
        sqrt_goldenratio = calculate_apothem(self.base_length_east, self.height) / self.height
        slope_angle = calculate_slope_angle(self.base_length_north, self.height)

        # Your methods
        my_method_1 = (
            math.sin(self.base_length_north / (self.base_length_east / 2) / self.height) * self.base_length_north
        )
        half_base = self.base_length_north / 2
        my_method_2 = (
            calculate_apothem(self.base_length_east, self.height)
            - calculate_edge(self.base_length_north, self.height)
            + (self.base_length_north / self.height * self.base_length_east / half_base)
        )
        edge = calculate_edge(self.base_length_north, self.height)
        my_method_3 = abs(math.sin(math.log(self.base_length_east)) - edge) / half_base

        return {
            'pivalue': pivalue,
            'goldenratio': goldenratio,
            'sqrt_goldenratio': sqrt_goldenratio,
            'difference_from_pi': abs(pivalue - PI),
            'difference_from_phi': abs(goldenratio - PHI),
            'slope_angle': slope_angle,
            'my_method_1_pi': my_method_1,
            'my_method_2_pi': my_method_2,
            'my_method_3_golden_ratio': my_method_3,
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

    @staticmethod
    def list_pyramids():
        return {pid: data["name"] for pid, data in PYRAMID_DATABASE.items()}

    def detailed_analysis(self, json=False):
        """
        Comprehensive analysis of the pyramid with constant comparisons
        """
        # Perform special calculations
        special_calcs = self.perform_special_calculations()

        analysis = {
            "name": self.name,
            "measurements": {
                "north_base_length": round(self.base_length_north, 2),
                "eastern_base_length": round(self.base_length_east, 2),
                "height": round(self.height, 2)
            },
            "special_calculations": {}
        }

        # Pi Value Comparison
        analysis["special_calculations"]["pi_value"] = {
            "calculated": round(special_calcs['pivalue'], 9),
            "actual": round(math.pi, 9),
            "difference_from_pi": round(abs(special_calcs['pivalue'] - math.pi), 9)
        }

         # Include new methods in the detailed analysis
        analysis["special_calculations"]["my_method_1_pi"] = {
            "calculated": round(special_calcs["my_method_1_pi"], 8),
            "difference_from_pi": round(abs(special_calcs["my_method_1_pi"] - math.pi), 8),
        }

        analysis["special_calculations"]["my_method_2_pi"] = {
            "calculated": round(special_calcs["my_method_2_pi"], 8),
            "difference_from_pi": round(abs(special_calcs["my_method_2_pi"] - math.pi), 8),
        }


        # Golden Ratio Comparison
        phi = (1 + np.sqrt(5)) / 2
        analysis["special_calculations"]["golden_ratio"] = {
            "calculated": round(special_calcs['goldenratio'], 9),
            "actual": round(phi, 9),
            "difference_from_phi": round(abs(special_calcs['goldenratio'] - phi), 9)
        }

        # Square Root of Golden Ratio Comparison
        sqrt_phi = np.sqrt(phi)
        analysis["special_calculations"]["sqrt_golden_ratio"] = {
            "calculated": round(special_calcs['sqrt_goldenratio'], 9),
            "actual": round(sqrt_phi, 9),
            "difference_from_sqrt_phi": round(abs(special_calcs['sqrt_goldenratio'] - sqrt_phi), 9)
        }

        analysis["special_calculations"]["my_method_3_golden_ratio"] = {
            "calculated": round(special_calcs["my_method_3_golden_ratio"], 8),
            "difference_from_Golden_ratio": round(abs(special_calcs["my_method_3_golden_ratio"] - ((1 + np.sqrt(5)) / 2) ), 8),
        }
        

        # Slope Angle
        analysis["special_calculations"]["slope_angle"] = round(special_calcs['slope_angle'], 2)

        # CG and Base Length Comparison
        cg_ratio, cg_difference = self.compare_CG_base_length()
        analysis["special_calculations"]["cg_base_length_comparison"] = {
            "calculated": round(cg_ratio, 9),
            "difference_from_sqrt2": round(cg_difference, 9)
        }

        # Tribonacci Constant Calculation and Comparison
        tribonacci_constant, tribonacci_difference = self.compare_tribonacci_constant()
        analysis["special_calculations"]["tribonacci_constant"] = {
            "calculated": round(tribonacci_constant, 9),
            "actual": 1.8393,
            "difference_from_tribonacci_constant": round(tribonacci_difference, 9)
        }

        # Root 5 Calculation and Comparison
        root_5_ratio, root_5_difference = self.compare_root_5()
        analysis["special_calculations"]["root_5_comparison"] = {
            "calculated": round(root_5_ratio, 9),
            "actual": round(np.sqrt(5), 9),
            "difference_from_sqrt5": round(root_5_difference, 9)
        }

        # Root 3 Calculation and Comparison
        root_3_ratio, root_3_difference = self.compare_root_3()
        analysis["special_calculations"]["root_3_comparison"] = {
            "calculated": round(root_3_ratio, 9),
            "actual": round(np.sqrt(3), 9),
            "difference_from_sqrt3": round(root_3_difference, 9)
        }

        # Golden Ratio - 1 Comparison
        golden_ratio_minus_1_ratio, golden_ratio_minus_1_difference = self.compare_golden_ratio_minus_1()
        analysis["special_calculations"]["golden_ratio_minus_1_comparison"] = {
            "calculated": round(golden_ratio_minus_1_ratio, 9),
            "actual": round(phi - 1, 9),
            "difference_from_phi_minus_1": round(golden_ratio_minus_1_difference, 9)
        }

       
        

        # Return JSON if specified
        if json:
            return analysis  # Ensure json is not overridden
        else:
            # Otherwise, print analysis (same as before)
            print(f"Detailed Analysis of {self.name}:")
            print("\nMeasurements and Calculated Values:")
            for key, value in analysis["measurements"].items():
                print(f"{key.replace('_', ' ').capitalize()}: {value:.2f} ft")

            print("\nSpecial Calculations vs Mathematical Constants:")
            for key, value in analysis["special_calculations"].items():
                print(f"\n{key.replace('_', ' ').capitalize()}:")
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        print(f"  {sub_key.replace('_', ' ').capitalize()}: {sub_value:.9f}")
                else:
                    print(f"  {key.replace('_', ' ').capitalize()}: {value:.9f}")

            return None