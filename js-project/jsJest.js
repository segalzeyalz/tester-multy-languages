const describe = (description, fn) => {
  console.log(description)
  fn()
}

const it = (msg, fn) => describe(`   ${msg}`, fn)

const matchers = (exp) => ({
  toBe: (assertion) => {
    if(exp == assertion) {
      console.log("pass")
      return true
    } else {
      console.log("fail")
      return false
    }
  }
})

const expect = (exp) => matchers(exp)

const addr = (a,b) => {
  if ((typeof a==="number") && (typeof b==="number")){
    return a+b
  }
    throw new Error("You must use only numbers as func params")
}

describe("addr", () => {
  it("adds two numbers", ()=>{
    const res = addr(1,4)
    expect(res).toBe(5)
  })
  it("Should add two negative numbers correctly", ()=>{
    const res = addr(-1, -5)
    expect(res).toBe(-6)
  })
  it("Should throw error", ()=>{
    res = addr(-1, "lala")
    expect(res).toBe("-1lala")

  })

})
