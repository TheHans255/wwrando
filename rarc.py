
import os
from io import BytesIO

from fs_helpers import *
from yaz0_decomp import Yaz0Decompressor

from dzx import DZx
from events import EventList
from bmg import BMG

class RARC:
  def __init__(self, file_path):
    self.file_path = file_path
    with open(self.file_path, "rb") as file:
      self.data = BytesIO(file.read())
    
    if try_read_str(self.data, 0, 4) == "Yaz0":
      self.data = BytesIO(Yaz0Decompressor.decompress(self.data))
    
    data = self.data
    
    self.file_data_list_offset = read_u32(data, 0xC) + 0x20
    num_nodes = read_u32(data, 0x20)
    node_list_offset = 0x40
    file_entries_list_offset = read_u32(data, 0x2C) + 0x20
    self.string_list_offset = read_u32(data, 0x34) + 0x20
    
    self.nodes = []
    for node_index in range(0, num_nodes):
      offset = node_list_offset + node_index*0x10
      node = Node(data, offset)
      self.nodes.append(node)
    
    self.file_entries = []
    self.dzx_files = []
    self.event_list_files = []
    self.bmg_files = []
    for node in self.nodes:
      for file_index in range(node.first_file_index, node.first_file_index+node.num_files):
        file_entry_offset = file_entries_list_offset + file_index*0x14
        
        file_entry = FileEntry(data, file_entry_offset, self)
        self.file_entries.append(file_entry)
        node.files.append(file_entry)
        
        if file_entry.id == 0xFFFF:
          # Directory
          continue
        
        if file_entry.name.endswith(".dzs"):
          dzx = DZx(file_entry)
          self.dzx_files.append(dzx)
        elif file_entry.name.endswith(".dzr"):
          dzx = DZx(file_entry)
          self.dzx_files.append(dzx)
        elif file_entry.name == "event_list.dat":
          event_list = EventList(file_entry)
          self.event_list_files.append(event_list)
        elif file_entry.name.endswith(".bmg"):
          bmg = BMG(file_entry)
          self.bmg_files.append(bmg)
  
  def extract_all_files_to_disk(self, output_directory=None):
    if output_directory is None:
      output_directory, _ = os.path.splitext(self.file_path)
    
    root_node = self.nodes[0]
    self.extract_node_to_disk(root_node, output_directory)
  
  def extract_node_to_disk(self, node, path):
    if not os.path.isdir(path):
      os.mkdir(path)
    
    for file in node.files:
      if file.id == 0xFFFF:
        # Directory
        if file.name not in [".", ".."]:
          subdir_path = os.path.join(path, file.name)
          subdir_node = self.nodes[file.node_index]
          self.extract_node_to_disk(subdir_node, subdir_path)
      else:
        file_path = os.path.join(path, file.name)
        file.data.seek(0)
        with open(file_path, "wb") as f:
          f.write(file.data.read())
  
  def save_to_disk(self):
    for file_entry in self.file_entries:
      if file_entry.id == 0xFFFF: # Directory
        continue
      self.data.seek(file_entry.data_offset + self.file_data_list_offset)
      file_entry.data.seek(0)
      self.data.write(file_entry.data.read())
    
    with open(self.file_path, "wb") as file:
      self.data.seek(0)
      file.write(self.data.read())

class Node:
  def __init__(self, data, offset):
    self.type = read_str(data, offset, 4)
    self.name_offset = read_u32(data, offset+4)
    self.unknown = read_u16(data, offset+8)
    self.num_files = read_u16(data, offset+0xA)
    self.first_file_index = read_u32(data, offset+0xC)
    
    self.files = [] # This will be populated after the file entries have been read.

class FileEntry:
  def __init__(self, data, offset, rarc):
    self.id = read_u16(data, offset)
    self.name_offset = read_u16(data, offset + 6)
    data_offset_or_node_index = read_u32(data, offset + 8)
    self.data_size = read_u32(data, offset + 0xC)
    self.name = read_str_until_null_character(data, self.name_offset+rarc.string_list_offset)
    
    if self.id == 0xFFFF:
      # Directory
      self.node_index = data_offset_or_node_index
      self.data = None
    else:
      self.data_offset = data_offset_or_node_index
      data.seek(self.data_offset+rarc.file_data_list_offset)
      self.data = BytesIO(data.read(self.data_size))
      if try_read_str(self.data, 0, 4) == "Yaz0":
        self.data = BytesIO(Yaz0Decompressor.decompress(self.data))
