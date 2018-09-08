#
#
# Created By : Mitchell Van Swol
# Date : 9/7/2018
#

# given a path string simplify path
class Solution(object):
    def simplifyPath(self, path):

        path_objs = path.split('/')
        curr_path = []
        for obj in path_objs:
            if obj == '..':
                if len(curr_path):
                    curr_path.pop()
            elif obj and obj != '.':
                curr_path.append(obj)

        new_path = '/' + '/'.join(curr_path)
        return new_path