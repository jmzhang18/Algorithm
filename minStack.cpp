class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {

    }
    
    void push(int x) {
        main_stack.push(x);
        if (min_stack.size()==0 || x <= min_stack.top()){
            min_stack.push(x);
        }
    }
    
    void pop() {
        if (main_stack.size()!=0){
            if (min_stack.size()!=0){
                if (main_stack.top() == min_stack.top()){
                    min_stack.pop();
                }
            }
            main_stack.pop();
        }
    }
    
    int top() {
        return main_stack.top();
    }
    
    int getMin() {
        return min_stack.top();
    }
private:
    std::stack<int> main_stack;
    std::stack<int> min_stack;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */