"""
Author: Aviraj Saha
Date: 2-10-2023
Purpose: Module contaning functions for updating and restoring markdown content.
"""


# Metadata
__author__: str = "Aviraj Saha"
__description__: str = "Module contaning functions for updating and restoring markdown content."
__all__: tuple[str] = ("update", "restore","main",)
__depedencies__: tuple[str] = (
    "python_standard_libs",
)
__keywords__: tuple[str] = ("__author__", "__description__", "__all__", "__depedencies__", "__keywords__",
                "update", "restore", "main")


from logging import basicConfig, warning, WARNING

basicConfig(level=WARNING)


def update(md_live_path: str, **data: dict[str: str]) -> None:
    """
    Updates live.md file with the latest values provided.
    """
    with open(md_live_path, 'r') as file:
        md_content = file.read()
        invalid_placeholders =[]
    for key in data.keys():
        if key not in md_content:
            invalid_placeholders.append(key)

    if invalid_placeholders:
        raise ValueError(f"Placeholders {invalid_placeholders} in not found in {md_live_path}")

    # Replace placeholders in the Markdown content with actual values
    for placeholder, value in data.items():
        md_content = md_content.replace(f'[{placeholder}]', str(value))

    # Write the updated content back to the file
    with open(md_live_path, 'w') as file:
        file.write(md_content)

    # warning(f"Placeholders have been replaced with actual values at {md_live_path}.")


def restore(*, md_live_path: str, md_backup_path: str) -> None:
    """
    Restores markdown content from md_live_path to md_backup_path.
    """
    with open(md_backup_path, 'r') as backup_file:
        md_backup_content = backup_file.read()

        with open(md_live_path, 'w') as live_file:
            live_file.write(md_backup_content)

    # warning(f'MD content has been restored from {md_backup_path}, to {md_live_path}')


def main() -> None:
    update(md_live_path="markdown/live.md", 
        Temperature_Readings = '30°C'
        )

    restore(md_live_path='markdown/live.md', md_backup_path='markdown/backup.md')


if __name__ == '__main__':
    main()