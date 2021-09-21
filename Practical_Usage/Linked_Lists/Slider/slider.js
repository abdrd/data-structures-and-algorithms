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
        text: "A donkey",
    },
]

const right = document.getElementById("right")
const left = document.getElementById("left")
const img = document.getElementById("img")
const text = document.getElementById("text")

class Card {
    constructor(img, text) {
        this.img = img
        this.text = text
        this.next = undefined
        this.prev = undefined
    }
}

class Slider {
    constructor() {
        this.head = undefined
        this.current = undefined
        this.size = 0
    }

    // redraw dom
    refresh() {
        img.src = this.current.img
        text.innerText = this.current.text
    }

    append(card) {
        if (this.size === 0) {
            this.head = card
            this.current = this.head
            this.size++
        } else if (this.size === 1) {
            this.head.next = card
            card.prev = this.head
            this.size++
        } else {
            let cur = this.head
            while (cur.next) {
                cur = cur.next
            }

            card.prev = cur
            cur.next = card

            this.size++
        }
    }

    swipeToRight() {
        if (this.size < 2) return
        if (!this.current.next) return
        else {
            this.current = this.current.next
            this.refresh()
        }
    }
    swipeToLeft() {
        if (this.size < 2) return
        if (!this.current.prev) return
        else {
            this.current = this.current.prev
            this.refresh()
        }
    }
}

const s = new Slider()

const c1 = new Card(DATA[0].img, DATA[0].text)
const c2 = new Card(DATA[1].img, DATA[1].text)
const c3 = new Card(DATA[2].img, DATA[2].text)
const c4 = new Card(DATA[3].img, DATA[3].text)

s.append(c1)
s.append(c2)
s.append(c3)
s.append(c4)

right.addEventListener("click", () => {
    s.swipeToRight()
})

left.addEventListener("click", () => {
    s.swipeToLeft()
})
