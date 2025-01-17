# PyramidMath - A Python Package for Pyramid Geometry and Mathematical Constants

`pyramid_math` is a Python package for analyzing the geometrical properties and mathematical constants of pyramids. It provides tools for calculating various attributes such as apothem, edge length, slope angle, and comparisons with mathematical constants like π (Pi), φ (Golden Ratio), and Tribonacci constant.

## Features

- Calculate geometrical properties of pyramids (e.g., apothem, edge, slope angle).
- Compare pyramid measurements with known mathematical constants.
- Predefined database of famous pyramids (e.g., Great Pyramid of Giza, Pyramid of Khafre, and more).
- Supports both predefined pyramids and custom pyramids with user-defined measurements.

## Installation

You can install the package via `pip` from PyPI:

```bash
pip install pyramid_math
```

## Usage

Once installed, you can use the package to analyze various pyramids. Here’s how to get started:

### Importing the Package

```python
from pyramid_math.pyramid import Pyramid
```

### Predefined Pyramid Example

You can use one of the predefined pyramids from the database:

```python
# Load the Great Pyramid of Giza from the predefined database
giza = Pyramid.from_database("great_pyramid_giza")

# Perform detailed analysis
giza.detailed_analysis()
```

This will output a detailed analysis of the Great Pyramid, including the comparison with mathematical constants like Pi, Golden Ratio, Tribonacci constant, and others.

### Custom Pyramid Example

You can also create your own custom pyramid by providing its measurements:

```python
# Create a custom pyramid with specified measurements (base lengths and height)
pyramid = Pyramid("Test Pyramid", 100, 100, 50)

# Perform special calculations on the custom pyramid
special_calcs = pyramid.perform_special_calculations()
print(special_calcs)
```

**Example Output:**

```python
{
    'pivalue': 3.0000,
    'goldenratio': 1.6180,
    'sqrt_goldenratio': 0.7273,
    'difference_from_pi': 0.0000,
    'difference_from_phi': 0.0000,
    'slope_angle': 26.5651
}
```

### List Available Pyramids

You can list all available pyramids from the predefined database:

```python
# List all available pyramids in the database
pyramids = Pyramid.list_pyramids()
print(pyramids)
```

**Example Output:**

```python
{
    'great_pyramid_giza': 'Great Pyramid of Giza (Pyramid of Khufu)',
    'pyramid_khafre': 'Pyramid of Khafre',
    'red_pyramid': 'Red Pyramid',
    'bent_pyramid': 'Bent Pyramid',
    'pyramid_menkaure': 'Pyramid of Menkaure',
    'sun_pyramid_teotihuacan': 'Pyramid of the Sun',
    'pyramid_coba': 'Pyramid of Coba',
    'nubian_pyramids': 'Nubian Pyramids of Meroe'
}
```

### Comparing Multiple Pyramids

You can compare measurements of multiple pyramids from the database:

```python
# Compare the Great Pyramid of Giza and the Pyramid of Khafre
comparison = Pyramid.compare_pyramids("great_pyramid_giza", "pyramid_khafre")
print(comparison)
```

**Example Output:**

```python
{
    'Great Pyramid of Giza (Pyramid of Khufu)': {
        'height': 481.0,
        'base_length': 756.0,
        'slope_angle': 51.84,
        'pi_ratio': 3.1454,
        'golden_ratio': 1.6180
    },
    'Pyramid of Khafre': {
        'height': 448.0,
        'base_length': 706.0,
        'slope_angle': 53.13,
        'pi_ratio': 3.1457,
        'golden_ratio': 1.6182
    }
}
```

## Mathematical Constants and Comparisons

The package compares the following constants:

- **π (Pi)**: The ratio of the base perimeter to the height of the pyramid.
- **φ (Golden Ratio)**: The ratio of the edge length to half of the base length.
- **Tribonacci Constant**: A constant derived from the geometry of the pyramid.
- **√5, √3**: Square roots of mathematical constants, compared with pyramid measurements.

### Detailed Analysis Output

When running the `detailed_analysis()` method, you will get comprehensive output that compares various calculations of the pyramid to well-known mathematical constants.

**Example Output:**

```bash
Detailed Analysis of Great Pyramid of Giza:
Measurements and Calculated Values:
North Base Length: 756.00 ft
Eastern Base Length: 756.00 ft
Height: 481.00 ft

Special Calculations vs Mathematical Constants:
(North base + Eastern base) / Height = 3.1454
Actual π value = 3.1416
Difference from π = 0.0038

Edge / (Base length / 2) = 1.6180
Actual φ (Golden Ratio) = 1.6180
Difference from φ = 0.0000

Apothem / Height = 0.7273
Actual √φ = 0.8510
Difference from √φ = 0.1237

Pyramid Slope Angle: 51.84 degrees

calculate_diagonal  (CG) / Base Length = 0.9220
Difference from √2 = 0.0214

Calculated Tribonacci Constant = 1.8393
Actual Tribonacci Constant = 1.8393
Difference from Tribonacci Constant = 0.0000

(Base Length + Apothem) / Apothem = 2.6180
Actual √5 = 2.2361
Difference from √5 = 0.3819

(Height + CG + CG) / (North Base + Eastern Base) = 1.7321
Actual √3 = 1.7321
Difference from √3 = 0.0000

Apothem / (Apothem + Half Base Length) = 0.6180
Actual φ - 1 = 0.6180
Difference from φ - 1 = 0.0000
```

### CG (Center of Gravity)

Note: In this package, **CG** refers to the **diagonal** of the pyramid, not the center of gravity. This is used in comparisons to constants like √2 and Tribonacci.

**Repository Views** ![Views](https://profile-counter.glitch.me/pyramidmath/count.svg)

## Contributing

Feel free to contribute by creating pull requests, reporting issues, or submitting feature requests.

## License

MIT License. See the [LICENSE](LICENSE) file for details.
