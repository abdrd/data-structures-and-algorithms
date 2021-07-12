export class Node {
    constructor(value) {
        this.value = value
        this.next = undefined
    }
}

export class LinkedList {
    constructor() {
        this.head = undefined
        this.size = 0
    }

    append(value) {
        const nodeToAppend = new Node(value)
        if (this.size === 0) {
            this.head = nodeToAppend
            this.size++
        } else {
            let cur = this.head
            while (cur.next) {
                cur = cur.next
            }
            cur.next = nodeToAppend
            this.size++
        }
    }
}
