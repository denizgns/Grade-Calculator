#Student Name: Deniz Güneş
# you will penalized if you forget to write your name here
#Author(s): Ayca Tuzmen, Umur Berkay Karakas

##### Enter Constants Here ###
HW_MIN = 0
HW_MAX = 100
Q_MIN = 0
Q_MAX = 100
F_MIN = 0
F_MAX = 100
A_MIN = 0
A_MAX = 15
#### End of Constants #######

##### Enter Imports Here ###
import math
#### End of Imports #######

def get_user_input(hw1, hw2, hw3, q1, q2, q3, att_grade, final_grade):
    """
    This function reads the inputs from the user for homework1, homework2, homework3,
    quiz1, quiz2, quiz3, attendance, final exam and returns their new values.
    The function should receive all the inputs.
    :param hw1: grade for homework1
    :param hw2: grade for homework2
    :param hw3: grade for homework3
    :param q1:  grade for quiz1
    :param q2:  grade for quiz2
    :param q3:  grade for quiz3
    :param att_grade: grade for attendance
    :param final_grade: grade for final exam
    :return: The function returns the values entered by user for
        homework1, homework2, homework3, quiz1, quiz2, quiz3, attendance, final exam
    """
    # i is a counter to keep track of taken grade types to run the while loop
    i = 0
    while i <= 3:
        grade_type = input('Please specify the grade type (H, Q, F, A): ')
        if grade_type == 'h' or grade_type == 'H':
            in1 = float(input('Please enter homework 1 grade: '))
            if in1 >= HW_MIN and in1 <= HW_MAX:
                hw1 = in1
            else:
                in1 = float(input('You entered a wrong value please re_enter hw1: '))
                hw1 = in1
            in2 = float(input('Please enter homework 2 grade: '))
            if in2 >= HW_MIN and in2 <= HW_MAX:
                hw2 = float(in2)
            else:
                in2 = input('You entered a wrong value please re_enter hw2: ')
                hw2 = in2
            in3 = float(input('Please enter homework 3 grade: '))
            if in3 >= HW_MIN and in3 <= HW_MAX:
                 hw3 = in3
            else:
                in3 = input('You entered a wrong value please re_enter hw3: ')
                hw3 = float(in3)
            i +=1
        elif grade_type == 'q' or grade_type == 'Q':
            in1 = float(input('Please enter quiz 1 grade: '))
            if in1 >= Q_MIN and in1 <= Q_MAX:
                q1 = in1
            else:
                while not (in1 >= Q_MIN and in1 <= Q_MAX):
                    in1 = float(input('You entered a wrong value please re_enter q1: '))
                q1 = in1
            in2 = float(input('Please enter quiz 2 grade: '))
            if in2 >= Q_MIN and in2 <= Q_MAX:
                q2 = float(in2)
            else:
                while not (in2 >= Q_MIN and in2 <= Q_MAX):
                    in2 = float(input('You entered a wrong value please re_enter q2: '))
                q2 = in2
            in3 = float(input('Please enter quiz 3 grade: '))
            if in3 >= Q_MIN and in3 <= Q_MAX:
                q3 = in3
            else:
                while not (in3 >= Q_MIN and in3 <= Q_MAX):
                    in3 = float(input('You entered a wrong value please re_enter q3: '))
                q3 = float(in3)
            i += 1
        elif grade_type == 'f' or grade_type == 'F':
            final_grade = float(input('Please enter final grade: '))
            if final_grade >= F_MIN and final_grade <=  F_MAX:
                final_grade = float(final_grade)
            else:
                while not (final_grade >= F_MIN and final_grade <=  F_MAX):
                    final_grade = float(input('You entered wrong, please reenter final'))
            i += 1
        elif grade_type == 'a' or grade_type == 'A':
            att_grade = float(input('Please enter attendance grade: '))
            if att_grade >= A_MIN and att_grade <= A_MAX:
                att_grade = float(att_grade)
            else:
                while not (att_grade >= A_MIN and att_grade <= A_MAX):
                    att_grade = float(input('You entered wrong, please reenter attendance'))
            i += 1
        else:
            print('Please enter a valid type')
    return hw1, hw2, hw3, q1, q2, q3, att_grade, final_grade



def show_total_grades(hw1, hw2, hw3, q1, q2, q3, att_grade, final_grade):
    """
    This function calculates the total grade using the input grades and shows on console
    the min, average and total grades.
    :param hw1: grade for homework1
    :param hw2: grade for homework2
    :param hw3: grade for homework3
    :param q1:  grade for quiz1
    :param q2:  grade for quiz2
    :param q3:  grade for quiz3
    :param att_grade: grade for attendance
    :param final_grade: grade for final exam
    :return: None

    """
    hw_ave = calculate_hw_ave(hw1, hw2, hw3)
    q_min = find_quiz_min(q1, q2, q3)
    quiz_ave = calculate_quiz_ave(q1, q2, q3)
    total_grade = calculate_total(hw_ave, quiz_ave, att_grade, final_grade)
    print('HW average: ', format(hw_ave, '.2f'))
    print('Minimum quiz grade:', format(q_min, '.2f'))
    print('Quiz average: ', format(quiz_ave, '.2f'))
    print('Total grade: ', format(total_grade, '.2f'))

def calculate_total (hw_ave, quiz_ave, att_grade, final_grade):
    """
    The function calculates the total grade using a formula given in pdf
    and return the total grade.
    :param hw_ave: averaga of 3 homeworks
    :param quiz_ave: average of 2 quizzes
    :param att_grade: attendance grade
    :param final_grade: final grade
    :return: total grade
    """
    total_grade = (hw_ave * (0.25 ** quiz_ave)) + (math.sqrt(quiz_ave) * 30) + (final_grade * 0.3) +  \
        math.sin(att_grade)
    return total_grade

def calculate_hw_ave (hw1, hw2, hw3):
    """
    The function calculates the average of 3 homeworks.
    :param hw1: grade for homework1
    :param hw2: grade for homework2
    :param hw3: grade for homework3
    :return: average grade of 3 homeworks
    """
    hw_ave = (hw1 + hw2 + hw3)/3
    return hw_ave

def calculate_quiz_ave (q1, q2, q3):
    """
    The function calculates the average of 2 quizzes. The smallest grade for 3 quizzes id dropped
    and not included in the average calculation
    :param q1:  grade for quiz1
    :param q2:  grade for quiz2
    :param q3:  grade for quiz3
    :return: The average of two quizzes.
    """
    qmin = find_quiz_min(q1, q2, q3)
    q_total = q1 + q2 + q3 - qmin
    q_avg = q_total / 2
    return q_avg

def find_quiz_min (q1, q2, q3):
    """
    The function finds the minimum grade out of three quizzes.
    :param q1:  grade for quiz1
    :param q2:  grade for quiz2
    :param q3:  grade for quiz3
    :return: The minimum of three quizzes.
    """
    return min(q1, q2, q3)


def main():
    ### DO NOT Remove or UPDATE this section ####
    hw1 = None
    hw2 = None
    hw3 = None
    att_grade = None
    q1 = None
    q2 = None
    q3 = None
    final_grade = None

    print('This program receive input about student grade')
    ### END of section ####

    ##### Your code starts here ###
    grade_list = get_user_input(hw1, hw2, hw3, q1, q2, q3, att_grade, final_grade)
    #The code did not work without equaling the grades so I manually equalized the variables
    hw1 = grade_list[0]
    hw2 = grade_list[1]
    hw3 = grade_list[2]
    q1 = grade_list[3]
    q2 = grade_list[4]
    q3 = grade_list[5]
    att_grade = grade_list[6]
    final_grade = grade_list[7]

    show_total_grades(hw1, hw2, hw3, q1, q2, q3, att_grade, final_grade)
    #### Your code ends here #######

main()