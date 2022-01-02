import os
def find_files(suffix, path, all_files=[]):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
       
    """
     

    dirs = suffix
    if path:
        dirs = suffix + '/' + path
    for x in os.listdir(dirs):
        temp_file = dirs + '/' + x
        if os.path.isfile(temp_file) and temp_file.endswith('.c'):
            all_files.append(temp_file)
            
        elif os.path.isdir(temp_file):
            all_files = find_files(dirs, x, all_files)
            
    return all_files


# Test cases with 'testdir'

print(find_files('.','testdir', all_files=[]))
print(find_files('.','',all_files=[]))
print(find_files('.','testdir/subdir1', all_files=[]))



 