#1-6-22
#
#GOAL:
#   Write a function to print ints and floats in form with commas or decimals.
#       I'm sure this exists in a much better form but I'd like to see if I can do it
#TODO:
#   -MAKE IT WORK WITH FLOATS
#   -GENERATE INSERTION_POINTS PROGRAMATICALLY BASED ON LEN
#   -THINK ABOUT DESIGN -- DOES IT NEED SOME MORE DEFAULT PARAMS?
#
#
######################################################################################
def pretty_print(string, code=0): #string is the number to be printed in string form; code is 0 for commas (1,000,000.98) | 1 for periods (1.000.000,98)
    if code:
        using = '.'
    else:
        using = ','

    nums = list(string)
    insertion_points = [3,7,11,15]

    #This part is dealing with floating points
    if '.' in nums: 
        important = len(nums)-3
        back_end = nums[-3:]
        nums = nums[:-3]
        print(nums,'   ',back_end)
    else:
        important = len(nums)
    #I reverse the nums list here after its already been processed because it can then be algorithmically filled with commas at the right place.
    # tentative big-O for this step is O(1) due to the size of the insertion_points array
    nums.reverse()
    for n in insertion_points:
        if n > important:
            break
        nums.insert(n,using)
    if using == '.':
        back_end[0] = ','
    nums.reverse()
    for item in back_end:
        nums.append(item)
    ans = ''.join(nums)
    print(ans)
   

    return ans


k = "218736687.99"
pretty_print(k)
pretty_print(k,1)
