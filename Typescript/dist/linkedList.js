"use strict";
var _a, _b, _c, _d, _e, _f;
var NNode = /** @class */ (function () {
    function NNode(value) {
        this.value = value;
        this.value;
    }
    return NNode;
}());
var LinkedList = /** @class */ (function () {
    function LinkedList() {
        this.size = 0;
    }
    LinkedList.prototype.nodeAt = function (index) {
        var cur = this.head;
        var curIndex = 0;
        if (cur) {
            if (index === curIndex)
                return cur;
            while (cur.next) {
                cur = cur.next;
                curIndex++;
                if (index === curIndex)
                    return cur;
            }
        }
        return null;
    };
    LinkedList.prototype.prepend = function (node) {
        if (this.size === 0)
            this.head = node;
        else
            node.next = this.head;
        this.head = node;
        this.size++;
    };
    LinkedList.prototype.append = function (node) {
        if (this.size === 0) {
            this.head = node;
            this.size++;
        }
        else if (this.size === 1 && this.head !== undefined) {
            this.head.next = node;
            this.size++;
        }
        else {
            var cur = this.head;
            while (cur === null || cur === void 0 ? void 0 : cur.next) {
                cur = cur.next;
            }
            cur.next = node;
            this.size++;
        }
    };
    LinkedList.prototype.insertAt = function (index, node) {
        var cur = this.head;
        var curIndex = 0;
        if (index === 0)
            this.prepend(node);
        if (this.head) {
            while (cur) {
                cur = cur.next;
                curIndex++;
                if (index === curIndex) {
                    var prevNode = this.nodeAt(curIndex - 1);
                    prevNode.next = node;
                    node.next = cur;
                    this.size++;
                }
            }
        }
    };
    LinkedList.prototype.pop = function () {
        if (this.size > 1) {
            var toPop = this.nodeAt(0);
            if (toPop === null || toPop === void 0 ? void 0 : toPop.next) {
                this.head = toPop.next;
                toPop.next = undefined;
            }
            else {
                this.head = undefined;
            }
            return toPop;
        }
        return null;
    };
    // TODO fix delete method ~~ I don't feel so good today
    LinkedList.prototype.delete = function (index) {
        if (index > this.size - 1)
            throw new Error("index out of range");
        if (this.size === 0)
            throw new Error("list is empty");
        if (index === 0) {
            this.pop();
            return;
        }
        var prevNode = this.nodeAt(index - 1);
        var nodeToDelete = this.nodeAt(index);
        if (nodeToDelete === null || nodeToDelete === void 0 ? void 0 : nodeToDelete.next) {
            prevNode.next = nodeToDelete === null || nodeToDelete === void 0 ? void 0 : nodeToDelete.next;
            nodeToDelete.next = undefined;
        }
        else
            prevNode.next = undefined;
    };
    return LinkedList;
}());
/***** TESTS *****/
var l = new LinkedList();
var n1 = new NNode("FIRST NODE");
l.prepend(n1);
/*
console.log(l.size);
console.log(l.head!.value);
*/
var n2 = new NNode("BEFORE FIRST NODE");
l.prepend(n2);
/*
console.log(l.head!.value);
console.log(l.head!.next!.value);
*/
var n3 = new NNode("LAST");
l.append(n3);
//console.log(l.head?.next?.next?.value);
/*
console.log(l.nodeAt(0)?.value);
console.log(l.nodeAt(1)?.value);
console.log(l.nodeAt(2)?.value);
*/
var n4 = new NNode("INSERT AT");
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
l.delete(3);
console.log((_c = (_b = (_a = l.head) === null || _a === void 0 ? void 0 : _a.next) === null || _b === void 0 ? void 0 : _b.next) === null || _c === void 0 ? void 0 : _c.value);
console.log((_f = (_e = (_d = l.head) === null || _d === void 0 ? void 0 : _d.next) === null || _e === void 0 ? void 0 : _e.next) === null || _f === void 0 ? void 0 : _f.next);
