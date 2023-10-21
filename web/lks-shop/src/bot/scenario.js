// ============ Utility Section ===================
// ================================================

// setCookie: set a cookie (mostly the Flag) at the Bot's browser
const setCookie = async (botData) => {
    const COOKIE_DOMAIN = process.env.COOKIE_DOMAIN || "localhost";
    const COOKIE_KEY = process.env.COOKIE_KEY || "flag";
    const COOKIE_VALUE = process.env.COOKIE_VALUE || "null";

    console.log(`[${botData.ip}][${botData._num}] [+] Setting Up Customized Cookie`);
    await botData.page.setCookie({
        name: COOKIE_KEY,
        value: COOKIE_VALUE,
        domain: COOKIE_DOMAIN,
        expire: 0,
        path: "/",
        httpOnly: false,
        secure: false,
        sameSite: "Lax"
    });
};

const doLogin = async (botData) => {
    const ADMIN_USERNAME = process.env.ADMIN_USERNAME || "admin";
    const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD || "admin";
    const url = new URL('/accounts/login/', botData.url);
    
    console.log(`[+] Opening login`);
    await botData.page.goto(url.href, { waitUntil: 'networkidle2' });
    await botData.page.focus('input[name="username"]');
    await botData.page.keyboard.type(ADMIN_USERNAME);
    await botData.page.focus('input[name="password"]');
    await botData.page.keyboard.type(ADMIN_PASSWORD);
    await botData.page.keyboard.press('Enter');
    await botData.page.waitForNavigation({waitUntil: 'networkidle2'});
}

const doTambahDuit = async (botData) => {
    const url = new URL('/tambah-duit-admin/', botData.url);

    console.log(`[+] Opening tambah-duit`);
    await botData.page.goto(url.href, { waitUntil: 'networkidle2' });
}

const doLogout = async (botData) => {
    const url = new URL('/accounts/logout/', botData.url);
    console.log(`[+] Opening logout`);
    await botData.page.goto(url.href, { waitUntil: 'networkidle2' });    
}

// execJavascript: evaluate JavaScript in the Bot's browser context (run JS in Bot's browser console)
const execJavascript = async (botData, jsFunc) => {
    console.log(`[${botData.ip}][${botData._num}] [+] Executing JavaScript`);
    await botData.page.evaluate(jsFunc);
};

// monitorBrowserRequest: print out every HTTP request performed by Bot's browser when visiting a URL
const monitorBrowserRequest = async (botData) => {
    await botData.page.on('request', req => {
        console.log(`[+] Browser is requesting to ${req.url()}`);
    });
}

// monitorConsoleOutput: print out Bot's browser console output
const monitorConsoleOutput = async (botData) => {
    await botData.page.on('console', async msg => {
        msg.args().forEach(arg => {
            arg.jsonValue().then(_arg => {
                console.log(`[$] Console Output: `, _arg);
            });
        });
    });
}

// ============ End of Utility Section ============
// ================================================

// ----------------------------------------------------------------- //

// ============ Scenario Section ==================
// ================================================

const beforeVisit = async (botData) => {
    console.log(`[+] Executing Pre-visit Bot Scenario`);
    // ======= Compose Bot scenario here to be ran before the URL is visited =======
    await doLogin(botData);
    await doTambahDuit(botData);
    monitorBrowserRequest(botData);
    //////////////////////////////////////////////////////////////////////////////////
};

const afterVisit = async (botData) => {
    console.log(`[+] Executing Post-visit Bot Scenario`);
    // ======= Compose Bot scenario here to be ran after the URL has been visited =======
    doLogout(botData);
    //////////////////////////////////////////////////////////////////////////////////
};

// ============ End of Scenario Section ===========
// ================================================

module.exports = {
    beforeVisit,
    afterVisit
};