from PIL import Image, IptcImagePlugin

image_path = "C:\\Users\\Bo\\Downloads\\1\\xxx\\Test_3.jpg"

iptc_fields = {
    'Object Name': 0x05,
    'Edit Status': 0x07,
    'Editorial Update': 0x08,
    'Urgency': 0x0A,
    'Category': 0x0F,
    'Supplemental Categories': 0x14,
    'Fixture Identifier': 0x16,
    'Keywords': 0x19,
    'Content Location Code': 0x1A,
    'Content Location Name': 0x1B,
    'Release Date': 0x1E,
    'Release Time': 0x23,
    'Expiration Date': 0x25,
    'Expiration Time': 0x26,
    'Special Instructions': 0x28,
    'Action Advised': 0x2D,
    'Reference Service': 0x2F,
    'Date Created': 0x37,
    'Time Created': 0x38,
    'By-line': 0x50,
    'By-line Title': 0x55,
    'City': 0x5A,
    'Sublocation': 0x5C,
    'Province/State': 0x5F,
    'Country/Primary Location Code': 0x64,
    'Country/Primary Location Name': 0x65,
    'Original Transmission Reference': 0x67,
    'Headline': 0x69,
    'Credit': 0x6E,
    'Source': 0x73,
    'Copyright Notice': 0x74,
    'Contact': 0x76,
    'Caption/Abstract': 0x78,
    'Writer/Editor': 0x7A,
    'Rasterized Caption': 0x7D,
    'Image Type': 0x82,
    'Image Orientation': 0x83,
    'Language Identifier': 0x87,
    'Custom Field': 0xC6,
    'Model Version': 0x00,
    'Destination': 0x05,
    'File Format': 0x14,
    'File Format Version': 0x16
}

image = Image.open(image_path)
info = IptcImagePlugin.getiptcinfo(image) or {}

for field, hex_value in iptc_fields.items():
    value = info.get((2, hex_value))
    print(f"Tag: {field} (Hex-Wert: {hex(hex_value)})")
    print(f"Value: {value.decode() if value and isinstance(value, bytes) else 'Leer'}")

image.close()
