const sucessWriter = () => {
    console.info("pass")
    return true
}

const failureWriter = () => {
    console.error("fail")
    return false
}

const conditionLoggerWritter = (condition) => {
    condition ? sucessWriter() : failureWriter()
}

const matchers = (exp) => ({
    toBe: (assertion) => {
        const condition = exp === assertion
        conditionLoggerWritter(condition)
    },
    errToBe: (err) => {
        const condition = err.message === exp.message
        conditionLoggerWritter(condition)
    }
})

export const describe = (description, fn) => {
    console.info(description)
    fn()
}

export const it = (msg, fn) => describe(`   ${msg}`, fn)

export const expect = (exp) => matchers(exp)
