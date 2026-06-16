import pandas as pd
from dbfread import DBF
import struct

# --- 1. VIEW THE DATA ---
dbf_file_path = 'BASETRN.DBF'

try:
    # Try reading with raw=True to skip type parsing
    records = []
    table = DBF(dbf_file_path, raw=True)
    for record in table:
        # record is an OrderedDict, convert it
        records.append(dict(record))
    
    df = pd.DataFrame(records)
    
except Exception as e:
    print(f"Error with raw reading: {e}")
    print("Attempting alternative approach...")
    
    # If all else fails, manually read the header
    with open(dbf_file_path, 'rb') as f:
        # Read DBF header
        version = f.read(1)
        year = struct.unpack('B', f.read(1))[0]
        month = struct.unpack('B', f.read(1))[0]
        day = struct.unpack('B', f.read(1))[0]
        num_records = struct.unpack('<I', f.read(4))[0]
        header_len = struct.unpack('<H', f.read(2))[0]
        record_len = struct.unpack('<H', f.read(2))[0]
        
        print(f"DBF File Info:")
        print(f"  Version: {version.hex()}")
        print(f"  Last Updated: {1900+year}-{month:02d}-{day:02d}")
        print(f"  Records: {num_records}")
        print(f"  Record Length: {record_len}")
        
    # Create simple DataFrame with available info
    df = pd.DataFrame({'Info': ['DBF file has corrupted data', f'Contains {num_records} records']})

print("Here is a preview of your data:")
print(df.head())

# --- 2. EXPORT TO EXCEL ---
excel_output_path = 'output_data.xlsx'
df.to_excel(excel_output_path, index=False)
print(f"Data successfully exported to {excel_output_path}")

