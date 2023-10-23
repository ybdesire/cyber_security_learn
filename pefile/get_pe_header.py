import datetime
import pefile

filename = 'aaa.Installer.x64.exe'
filename = 'msvcp140_aaa.dll'

pe = pefile.PE(filename)
d =  pe.FILE_HEADER.dump_dict()
print(d)
'''
{
  'Structure': 'IMAGE_FILE_HEADER', 
  'Machine': {'FileOffset': 260, 'Offset': 0, 'Value': 34404}, 
  'NumberOfSections': {'FileOffset': 262, 'Offset': 2, 'Value': 6}, 
  'TimeDateStamp': {'FileOffset': 264, 'Offset': 4, 'Value': '0x61B17C2A [Thu Dec  9 03:46:50 2021 UTC]'}, 
  'PointerToSymbolTable': {'FileOffset': 268, 'Offset': 8, 'Value': 0},
  'NumberOfSymbols': {'FileOffset': 272, 'Offset': 12, 'Value': 0}, 
  'SizeOfOptionalHeader': {'FileOffset': 276, 'Offset': 16, 'Value': 240}, 
  'Characteristics': {'FileOffset': 278, 'Offset': 18, 'Value': 8226}
}
'''
