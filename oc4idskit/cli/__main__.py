import logging

from ocdskit.cli.__main__ import main as ocdskit_main


def main():
    modules = (
        "oc4idskit.cli.commands.convert_from_ocds",
        "oc4idskit.cli.commands.split_project_packages",
    )

    logger = logging.getLogger("oc4idskit")

    ocdskit_main(
        description="Open Contracting for Infrastructure Data Standards CLI",
        modules=modules,
        logger=logger,
    )


if __name__ == "__main__":
    main()
