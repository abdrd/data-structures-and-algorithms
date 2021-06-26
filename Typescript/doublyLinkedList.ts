// type NodeValue = string | boolean | number
// TODO implement doubly linked list in typescript

class NNNode<NodeValue> {
    value: NodeValue;
    next?: NNNode<NodeValue>;
    prev?: NNNode<NodeValue>;
    constructor(value: NodeValue) {
        this.value = value;
    }
}

class DoublyLinkedList {
    head?: NNNode<NodeValue>;
    size: number = 0;

    nodeAt(index: number) {
        let cur = this.head;
        let curIndex = 0;

        if (cur) {
            if (index === curIndex) return cur;
            while (cur.next) {
                cur = cur.next;
                curIndex++;

                if (index === curIndex) return cur;
            }
        }
        return null;
    }

    prepend(node: NNNode<NodeValue>) {
        if (this.size === 0) {
            this.head = node;
            return;
        } else {
            let prevHead = this.head;
            node.next = this.head;
            this.head = node;
            prevHead?.prev = node;
            this.size++;
        }
    }
}
