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

const addr = (a,b) => a+b

describe("addr", () => {
  it("adds two numbers", ()=>{
    const result = addr(1,4)
    expect(result).toBe(5)
  })
})
