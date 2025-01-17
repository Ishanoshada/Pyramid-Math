from .pyramid import Pyramid

def main():
    print("Welcome to PyramidMath!")
    pyramids = Pyramid.list_pyramids()
    print("\nAvailable pyramids:")
    for pid, name in pyramids.items():
        print(f"- {pid}: {name}")

    choice = input("\nEnter the pyramid ID to analyze: ").strip()
    try:
        pyramid = Pyramid.from_database(choice)
        pyramid.detailed_analysis()
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    main()
