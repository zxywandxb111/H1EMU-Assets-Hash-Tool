
"""
File Hash Calculator - For calculating official format CRC32 and SHA256
"""
import zlib
import hashlib
import os

def calculate_official_crc32(file_path):
    """Calculate official format CRC32 (reversed byte order)"""
    with open(file_path, 'rb') as f:
        data = f.read()
    
    crc32 = zlib.crc32(data)
    crc32 = crc32 & 0xFFFFFFFF
    
    # Convert to official format: reverse byte order
    s = hex(crc32)[2:].zfill(8)
    official_crc = s[6:8] + s[4:6] + s[2:4] + s[0:2]
    
    return official_crc

def calculate_sha256(file_path):
    """Calculate SHA256 hash"""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        # Read large files in chunks
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

def main():
    directory = r"D:\JustSurvive2016-20240420\Resources\Assets"
    
    print("=" * 60)
    print("File Hash Calculator")
    print("=" * 60)
    
    # Get all Assets pack files
    files = sorted([f for f in os.listdir(directory) 
                   if f.startswith('Assets_') and f.endswith('.pack')])
    
    print(f"\nFound {len(files)} files\n")
    print(f"{'Filename':&lt;20} {'Official CRC32':&lt;16} {'SHA256'}")
    print("-" * 100)
    
    for filename in files:
        filepath = os.path.join(directory, filename)
        
        try:
            crc32 = calculate_official_crc32(filepath)
            sha256 = calculate_sha256(filepath)
            
            print(f"{filename:&lt;20} {crc32:&lt;16} {sha256}")
        except Exception as e:
            print(f"{filename:&lt;20} Error: {str(e)}")

if __name__ == "__main__":
    main()
