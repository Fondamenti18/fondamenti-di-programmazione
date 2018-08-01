import re


def post(fposts, insieme):
    return set(
        [[post_info.lstrip().split("\n")[0].rstrip(), ' '.join(post_info.lstrip().split("\n")[1:]).lower()][0] for
         post_info in open(fposts, 'r').read().split("<POST>")[1:] if any(re.search(r'\b' + ext.lower() + r'\b', [
            post_info.lstrip().split("\n")[0].rstrip(), ' '.join(post_info.lstrip().split("\n")[1:]).lower()][1]) for
                                                                          ext in insieme)])
