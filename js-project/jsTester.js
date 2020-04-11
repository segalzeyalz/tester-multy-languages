export const describe = (description, fn) => {
    console.log(description)
    fn()
}

export const it = (msg, fn) => describe(`   ${msg}`, fn)

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

export const matchers = (exp) => ({
    toBe: (assertion) => {
        conditionLoggerWritter(exp === assertion)
    },
    errToBe: (err) => {
        conditionLoggerWritter(err.message === exp.message)
    }
})

export const expect = (exp) => matchers(exp)
