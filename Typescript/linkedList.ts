type NodeValue = string | number | boolean;

class NNode<NodeValue> {
    value: NodeValue;
    next?: NNode<NodeValue>;
    constructor(value: NodeValue) {
        this.value = value;
    }
}

class LinkedList {
    head?: NNode<NodeValue>;
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

    prepend(node: NNode<NodeValue>) {
        if (this.size === 0) {
            this.head = node;
            return;
        } else node.next = this.head;
        this.head = node;
        this.size++;
    }

    append(node: NNode<NodeValue>) {
        if (this.size === 0) {
            this.head = node;
            this.size++;
        } else if (this.size === 1 && this.head !== undefined) {
            this.head.next = node;
            this.size++;
        } else {
            let cur = this.head;

            while (cur?.next) {
                cur = cur.next;
            }

            cur!.next = node;

            this.size++;
        }
    }

    insertAt(index: number, node: NNode<NodeValue>) {
        let cur = this.head;
        let curIndex = 0;

        if (index === 0) this.prepend(node);

        if (this.head) {
            while (cur) {
                cur = cur.next;
                curIndex++;

                if (index === curIndex) {
                    let prevNode = this.nodeAt(curIndex - 1);
                    prevNode!.next = node;
                    node.next = cur;
                    this.size++;
                }
            }
        }
    }

    pop(): NNode<NodeValue> | null {
        if (this.size > 1) {
            let toPop = this.nodeAt(0);

            if (toPop?.next) {
                this.head = toPop.next;
                toPop.next = undefined;
            } else {
                this.head = undefined;
            }

            return toPop;
        }
        return null;
    }

    delete(index: number) {
        if (index > this.size - 1) throw new Error("index out of range");
        if (this.size === 0) throw new Error("list is empty");
        if (index === 0) {
            this.pop();
            return;
        }

        let prevNode = this.nodeAt(index - 1);
        let nodeToDelete = this.nodeAt(index);

        if (nodeToDelete?.next) {
            prevNode!.next = nodeToDelete?.next;
            nodeToDelete.next = undefined;
        } else prevNode!.next = undefined;
    }
}

/***** TESTS *****/
const l = new LinkedList();

const n1 = new NNode<string>("FIRST NODE");
l.prepend(n1);
/*
console.log(l.size);
console.log(l.head!.value);
*/
const n2 = new NNode("BEFORE FIRST NODE");
l.prepend(n2);
/*
console.log(l.head!.value);
console.log(l.head!.next!.value);
*/

const n3 = new NNode("LAST");
l.append(n3);

//console.log(l.head?.next?.next?.value);
/*
console.log(l.nodeAt(0)?.value);
console.log(l.nodeAt(1)?.value);
console.log(l.nodeAt(2)?.value);
*/

const n4 = new NNode("INSERT AT");
//l.insertAt(0, n4)
//console.log(l.head?.value);

l.insertAt(2, n4);
//console.log(l.head!.next?.next?.value);
/*
l.delete(0);
console.log(l.head?.value);
console.log(l.head?.next?.value);
*/
/*
l.delete(1);
console.log(l.head?.value);
console.log(l.head?.next?.value);
*/
/*
l.delete(3);
console.log(l.head?.next?.next?.value);
console.log(l.head?.next?.next?.next);
*/
