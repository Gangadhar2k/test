import sys
from minidump.minidumpfile import MinidumpFile


def read_minidump(minidump_path):
    print(minidump_path)

    minidump = MinidumpFile.parse(minidump_path)
    print(minidump)
    print("Module Information:")
    print("===================")

    # If modules are directly accessible via an attribute, e.g., minidump.modules
    print(minidump.modules)
    print("===================")
    print("Threads Information:")
    print("===================")
    print(minidump.threads)
    print("===================")
    print("Exception Information:")
    print("===================")
    print(minidump.exception)
    print("===================")
    print("comment_a Information:")
    print("===================")
    print(minidump.comment_a)
    print("===================")
    print("filename Information:")
    print("===================")
    print(minidump.filename)
    print("===================")
    print("file_handle Information:")
    print(minidump.file_handle)
    print("===================")
    print("directories Information:")
    print(minidump.directories)
    print("===================")
    print("memory_info Information:")
    print(minidump.memory_info)
    print("===================")
    print("memory_segments Information:")
    print(minidump.memory_segments)
    print("===================")
    print("memory_segments_64 Information:")
    print(minidump.memory_segments_64)
    print("===================")
    print("thread_info Information:")
    print(minidump.thread_info)
    print("===================")
    print("threads_ex Information:")
    print(minidump.threads_ex)
    print("===================")
    print("__module__ Information:")
    print(minidump.__module__)
    print("===================")





if __name__ == "__main__":
    minidump_path = "C:\\Users\\Gangadhar\\Documents\\lsass.dmp"
    read_minidump(minidump_path)
