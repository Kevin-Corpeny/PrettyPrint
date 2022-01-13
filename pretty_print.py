#1-6-22
#
#UPDATED 1-13-22
#KAIMED
#GOAL:
#   Write a function to print ints and floats in form with commas or decimals.
#       I'm sure this exists in a much better form but I'd like to see if I can do it
#TODO:
#    DONE -MAKE IT WORK WITH FLOATS
#    DONE -GENERATE INSERTION_POINTS PROGRAMATICALLY BASED ON LEN 
#   -THINK ABOUT DESIGN -- DOES IT NEED SOME MORE DEFAULT PARAMS? PROBABLY NOT
#
#
#####################################################################################

def pretty_print(string, code=0):
    if type(string) != 'String':
        string = str(string)
    if code:
        using = '.'
    else:
        using = ','
    floatFlag = False
    nums = list(string)

    insertion_points = []
    
    
    #This part is dealing with floating points
    if '.' in nums: 
        important = len(nums)-3
        back_end = nums[-3:]
        nums = nums[:-3]

        floatFlag = True
        #print(nums,'   ',back_end) DEBUGGING
    else:
        important = len(nums)
    num_needed = (important-1) // 3
    index = 3
    for x in range(num_needed):
        insertion_points.append(index)
        index = index+4
    print(insertion_points)

    #I reverse the nums list here after its already been processed because it can then be algorithmically filled with commas at the right place.
    # tentative big-O for this step is O(1) due to the size of the insertion_points array
    nums.reverse()
    for n in insertion_points:
        if n > important:
            break
        nums.insert(n,using)
        important = important + 1
    if using == '.':
        back_end[0] = ','
    nums.reverse()
    if floatFlag: 
        for item in back_end:
            nums.append(item)
    ans = ''.join(nums)
    print(ans)
    print(important)   

    return ans

pretty_print(83983886859508388377)
k = "218736687.99"
pretty_print(k)
pretty_print(k,1)
pretty_print(90897987987898907908789786876896786786876986760766706780676876760867060)
