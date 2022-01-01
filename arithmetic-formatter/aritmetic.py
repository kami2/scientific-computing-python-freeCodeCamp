def arithmetic_arranger(problems, arg_result=False):

    if len(problems) > 5:
        return "Error: Too many problems."


    upper_list = []
    bottom_list = []
    dashes = []
    list_of_results = []


    for problem in problems:
        splitted_problems = problem.split()

        higher_number_length = max(len(splitted_problems[0]), len(splitted_problems[2]))
        lower_number_length = min(len(splitted_problems[0]), len(splitted_problems[2]))
        number_of_dash = higher_number_length + 2
        operator = splitted_problems[1]

        try:
            int(splitted_problems[0])
            int(splitted_problems[2])
        except:
            return "Error: Numbers must only contain digits."

        if higher_number_length > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+" or operator == "-":
            if "+" == operator:
                result = int(splitted_problems[0]) + int(splitted_problems[2])
                spaces_in_result = number_of_dash - len(str(result))
                list_of_results.append(spaces_in_result * " " + str(result))
            elif "-" == operator:
                result = int(splitted_problems[0]) - int(splitted_problems[2])
                spaces_in_result = number_of_dash - len(str(result))
                list_of_results.append(spaces_in_result * " " + str(result))
        else:
            return "Error: Operator must be '+' or '-'."


        if operator == "+" or operator == "-":
            if higher_number_length is len(splitted_problems[0]):
                spaces_for_top_numbers = higher_number_length - lower_number_length + 1
                bottom_list.append(splitted_problems[1] + spaces_for_top_numbers * " " + splitted_problems[2] + 4 * " ")

                number_of_space_bottom_list = number_of_dash - higher_number_length
                upper_list.append(number_of_space_bottom_list * " " + splitted_problems[0] + 4 * " ")

            else:
                number_of_space_upper = number_of_dash - lower_number_length
                upper_list.append(number_of_space_upper * " " + splitted_problems[0] + 4 * " ")

                spaces_for_bottom_numbers = number_of_dash - higher_number_length - 1
                bottom_list.append(splitted_problems[1] + spaces_for_bottom_numbers * " " + splitted_problems[2] + 4 * " ")
        else:
            return "Error: Operator must be '+' or '-'."

        dashes.append(number_of_dash * "-")


    a = "".join(upper_list)
    b = "".join(bottom_list)
    c = "    ".join(dashes)
    d = "    ".join(list_of_results)


    if arg_result:
        arranged_problems = a.rstrip() + '\n' + b.rstrip() + '\n' + c + '\n' + d
    else:
        arranged_problems = a.rstrip() + '\n' + b.rstrip() + '\n' + c


    return arranged_problems



arithmetic_arranger(['3801 - 2', '123 + 49'])



