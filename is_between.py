def is_between(string, start, end, iters=0, index=0, ind_break=True):
    # a function to search text and return whatever string is found between two specified strings
    # string = the text to be searched - in the CLI implementation, a file is used
    # start, end = the terms between which the result is found
    # iters = the number of instances being looked for, -1 searches for all existing instances
    # index = the index of the result desired
    # specify iters or index, NOT both; if neither is specified, the first result is returned
    # ind_break = if False, and specified index does not exist, last item in list will be returned
    # otherwise, None value will be returned
    return_list = []


    def more_present(str_, start_, end_):
        # checks if there are more of the search terms, and that they're in the correct order
        if start_ not in str_ or end_ not in str_:
            return False
        while str_.find(end) < str_.find(start):
            str_ = str_[str_.find(end) + len(end):]
        if str_.find(end) != -1:
            return True


    def find_index(str_, start_, end_):
        # returns the indexes at the beginning and end of the found string
        start_num = str_.find(start_) + len(start_)
        end_num = str_.find(end_, start_num)
        return start_num, end_num


    def perform_search(str_, start_, end_):
        # finds string between start_ and end_, returns str_ trimmed to begin after end_
        # and returns the found string
        if more_present(str_, start_, end_):
            start_no, end_no = find_index(str_, start_, end_)
            new_str = str_[end_no + len(end):]
            return new_str, (''.join(list(str_)[start_no:end_no]))
        else:
            raise ValueError


    def iterate_search(str_, start_, end_):
        # adds search term to the return_list, and trimmed string from perform_search
        nonlocal return_list
        str_, result = perform_search(str_, start_, end_)
        return_list.append(result)
        return str_

    if -2 >= iters or -1 >= index or (iters != 0 and index != 0):
        # invalid variable entry
        return None

    if not more_present(string, start, end):
        # nothing matches the search
        return  None

    if iters != 0:
        # returns a list of found terms up to and including the number of iterations
        try:
            if iters == -1:
                while True:
                    string = iterate_search(string, start, end)
            for _ in range(iters):
                string = iterate_search(string, start, end)
            return return_list
        except ValueError:
            return  return_list if return_list != [] else None

    if index is not None:
        try:
            while len(return_list) < index + 1:
                string = iterate_search(string, start, end)
            return return_list[index]
        except ValueError:
            # the desired index does not exist
            if ind_break:
                return None
            else:
                # if ind_break is set to False, returns last found string in the list
                return return_list[-1]


if __name__ == '__main__':
    import argparse


    cli_input = argparse.ArgumentParser(prog='is_between', description='Search for anything between two given strings')
    cli_input.add_argument('path', help='File to be searched within')
    cli_input.add_argument('start', help='The first term in the search')
    cli_input.add_argument('end', help='The closing term of the search')
    ind_iter_group = cli_input.add_mutually_exclusive_group()
    ind_iter_group.add_argument('-i', '--iters', type=int, default=0, help='Number of instances to return')
    ind_iter_group.add_argument('-n', '--index', type=int, default=0, help='Index of result to return')
    cli_input.add_argument('-b', '--ind_break', default=True, help='If False, and specified index does not exist, returns last found result; if True, returns None value')

    args = cli_input.parse_args()
    with open(args.path, 'r') as file_:
        print(is_between(file_.read(), args.start, args.end, args.iters, args.index, args.ind_break))

