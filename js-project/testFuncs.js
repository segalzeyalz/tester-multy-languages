import {describe, it, expect} from './jsTester.js'

const addr = (a, b) => {
    if ((typeof a === "number") && (typeof b === "number")) {
        return a + b
    }
    throw new Error("You must use only numbers as func params")
}

describe("addr", () => {
    it("adds two numbers", () => {
        const res = addr(1, 4)
        expect(res).toBe(5)
    })
    it("Should add two negative numbers correctly", () => {
        const res = addr(-1, -5)
        expect(res).toBe(-6)
    })
    it("Should throw error", () => {
        try {
            const res = addr(-1, "lala")
        } catch (err) {
            expect(err).errToBe(Error("You must use only numbers as func params"))
        }

    })
})
