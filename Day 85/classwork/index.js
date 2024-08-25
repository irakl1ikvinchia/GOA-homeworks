const cars = ["BMW", "audi", "mersedes", "man"]

// პოულობს რომელ ინდეხსზე არის გადაცემული მნიშვნელობა:
let index0 = fruits.indexof("audi")
let index1 = fruits.indexof("BMW")
let index2 = fruits.indexof("man")


// _________________________________________________

// ეძებს ყველაზე ბოლო ინდექსზე მყოფ ელემენტს:
let index3 = fruits.lastIndexof("mersedes")
let index4 = fruits.lastIndexof("audi")
let index5 = fruits.lastIndexof("BMW")


// __________________________________________________

// დაიწყებს ძებნას იმ ინდექსიდან რომელსაც გადავცემთ მეორე მნიშვნელობად:
let index6 = fruits.includes("mersedes", 2)
let index7 = fruits.includes("audi", 1)
let index8 = fruits.includes("BMW", 3)
