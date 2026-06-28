class MyQueue {
    int si[100];
    int sd[100];
    int top1;
    int top2;

public:
    MyQueue() {
        top1 = -1;
        top2 = -1;
    }

    void push(int x) {
        if (top1 >= 100 - 1) {
            cout << "Overflow" << endl;
            return;
        }
        si[++top1] = x;
    }

    int pop() {
    if (top2 == -1) {
        if (top1 == -1) {
            cout << "Underflow" << endl;
            return -1;
        }
        while (top1 != -1) {
            sd[++top2] = si[top1--];
        }
    }
    return sd[top2--];
}


    int peek() {
        if (top2 == -1) {
            if (top1 == -1) {
                cout << "Underflow" << endl;
                return -1;
            }
            while (top1 != -1) {
                sd[++top2] = si[top1--];
            }
        }
        return sd[top2];
    }

    bool empty() {
        return (top1 == -1 && top2 == -1);
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
