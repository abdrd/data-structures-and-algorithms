// TODO not complete

const DATA = [
    {
        img: "https://www.nawpic.com/media/2020/cute-cat-nawpic-7.jpg",
        text: "A cute kitten :)",
    },
    {
        img: "https://www.nawpic.com/media/2020/cute-cat-nawpic-1.png",
        text: "Another cute kitten :))",
    },
    {
        img: "https://cdn.shopify.com/s/files/1/0230/2984/1992/products/soccer-ball-on-green-grass-wall-mural_1200x630.jpg?v=1563395177",
        text: "A soccer ball",
    },
    {
        img: "https://cdn.mos.cms.futurecdn.net/6h8C6ygTdR2jyyUxkALwsc-1200-80.jpg",
        text: "A cute ass (donkey)",
    },
]

// a node in the linked list
class Card {
    img
    text
    next
    prev
    constructor(img, text) {
        this.img = img
        this.text = text
    }
}

// list
class Slider {
    // Card (head)
    head
    // current card displayed
    current
    size

    append(card) {
        if (this.size === 0) {
            this.head = card
            this.current = this.head
        }
        if (this.size === 1) {
            const head = this.head
            head.next = card
            card.prev = this.head
        }
        if (this.size > 1) {
            let cur = this.head

            while (cur.next) {
                cur = cur.next
            }
            cur.next = card
            card.prev = cur
        }
    }

    swipeToRight() {
        if (size < 2) return
        if (!this.current.next) return
        else {
            this.current = this.current.next
        }
    }

    swipeToLeft() {
        if (this.size < 2) return
        if (!this.current.prev) return
        else {
            this.current = this.current.prev
        }
    }
}

let slider = new Slider()

const c1 = new Card(DATA[0].img, DATA[0].text)
const c2 = new Card(DATA[1].img, DATA[1].text)
const c3 = new Card(DATA[2].img, DATA[2].text)
const c4 = new Card(DATA[3].img, DATA[3].text)

slider.append(c1)
slider.append(c2)
slider.append(c3)
slider.append(c4)

// * DOM manipulation

const imgTag = document.getElementById("img")
const textP = document.getElementById("text")
const right = document.getElementById("right")
const left = document.getElementById("left")

right.addEventListener("click", () => {
    slider.swipeToRight()
})

left.addEventListener("click", () => {
    slider.swipeToLeft()
})

imgTag.src = slider.current.img
textP.innerText = slider.current.text
