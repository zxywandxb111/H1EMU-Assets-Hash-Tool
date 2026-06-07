
# File Hash Calculator

A Python tool for calculating official-format CRC32 and SHA256 hashes for game asset files.

## Features

- Calculates official format CRC32 (handles reversed byte order)
- Calculates SHA256 hashes
- Batch processes all Assets_*.pack files
- Efficient large file handling

## Usage

```bash
python calculate_hashes.py
```

## Output Format

The script will output:
- Filename
- Official CRC32 (reversed byte order)
- SHA256 hash

## Official CRC32 Format

The official CRC32 format requires reversing the byte order of the standard CRC32 value:
- Standard CRC32: `0x7a1b23ac`
- Official format: `ac231b7a`

## Requirements

- Python 3.x
- No additional dependencies required
