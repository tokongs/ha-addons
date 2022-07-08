from home_assistant_cdf_extractor import __version__
from home_assistant_cdf_extractor.extractor import extractor


def main() -> None:
    with extractor:
        extractor.run()


if __name__ == "__main__":
    main()
