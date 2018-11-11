# NOTE: This is the first thing I've ever written in R!
# I had to learn R to solve this programming problem during the competition.
# I'm very proud of this code.

f <- file("stdin")
on.exit(close(f))

T <- readLines(f)
T <- strsplit(T, " ")

testcases <- as.numeric(T[[1]])

for(q in 1:testcases) {
    testcase_input = T[[q+1]]
    A = as.numeric(testcase_input[[1]])
    B = as.numeric(testcase_input[[2]])
    V = as.numeric(testcase_input[[3]])
    
    constants = pi/(4*A**2)
    f_of_y = function(x){
        return((4*A*log(x) + 2*B**2 - 2*B*sqrt(4*A*log(x)+B**2)))
    }
    
    goal = V
    accuracy = .2
    test_inp = 1
    test_result = integrate(f_of_y, 1, test_inp)[[1]]
        
    step_sizes = list(.01, .05, .1, .2, 1, 5, 10)
    step_pos = length(step_sizes)
    last_val = -1
    
    while (!((goal-accuracy) <=  test_result && test_result <= (goal+accuracy))) {
        poss_new_val = integrate(f_of_y, 1, test_inp+step_sizes[[step_pos]])[[1]]*constants
        #print(step_pos)
        #print(poss_new_val)
        if (poss_new_val > goal+accuracy){
            if(step_pos != 1){
                step_pos = step_pos - 1
                next
            }
        } else {
            test_inp = step_sizes[[step_pos]] + test_inp
            test_result = poss_new_val
        }
        #print("last")
        #print(last_val)
        #print("test")
        #print(test_result)
        # Check if the code is getting stuck in a loop
        # If it is, break, since the actual value is nearby
        if(last_val == test_result){
            break
        }
        last_val = test_result
    }
    
    # Test to see if there's a better fit nearby
    ret = test_inp
    min_err = abs(V - test_result)
    
    # Make sure the range of the inputs fit the range of the problem/function
    left_bound = max(1, test_inp-.5)
    for(i in seq(left_bound, test_inp+.5, .01)){
        res = integrate(f_of_y, 1, i)[[1]]*constants
        err = abs(V-res)
        if(err < min_err){
            min_err = err
            ret = i
        }
    }
    
    ret = format(round(ret, 2), nsmall = 2)
    write(ret, stdout())
}

