/**
 * Calculator Web UI Application
 * Professional calculator with simple and scientific modes
 */

class Calculator {
    constructor() {
        this.currentNumber = '0';
        this.previousNumber = null;
        this.operator = null;
        this.waitingForOperand = false;
        this.expression = '';
        this.lastResult = null;
        this.isScientificMode = false;

        // Constants
        this.PI = Math.PI;
        this.E = Math.E;

        // Scientific function names for display
        this.functionNames = {
            'sin': 'sin',
            'cos': 'cos',
            'tan': 'tan',
            'asin': 'sin⁻¹',
            'acos': 'cos⁻¹',
            'atan': 'tan⁻¹',
            'log': 'log',
            'ln': 'ln',
            'exp': 'e^',
            'sqrt': '√',
            'sqr': 'sqr',
            'cbrt': '∛',
            'inv': '1/',
            'abs': '|',
            'neg': '±',
            'fact': '!'
        };

        // DOM Elements
        this.calculator = document.getElementById('calculator');
        this.displayResult = document.getElementById('result');
        this.displayExpression = document.getElementById('expression');
        this.scientificButtons = document.getElementById('scientificButtons');
        this.simpleModeBtn = document.getElementById('simpleMode');
        this.scientificModeBtn = document.getElementById('scientificMode');

        this.init();
    }

    init() {
        // Button click handlers
        document.querySelectorAll('.btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.handleButtonClick(e));
        });

        // Mode toggle handlers
        this.simpleModeBtn.addEventListener('click', () => this.setMode('simple'));
        this.scientificModeBtn.addEventListener('click', () => this.setMode('scientific'));

        // Keyboard support
        document.addEventListener('keydown', (e) => this.handleKeyPress(e));

        // Load saved mode preference
        this.loadModePreference();
    }

    setMode(mode) {
        this.isScientificMode = mode === 'scientific';

        if (this.isScientificMode) {
            this.calculator.classList.add('scientific');
            this.scientificModeBtn.classList.add('active');
            this.simpleModeBtn.classList.remove('active');
        } else {
            this.calculator.classList.remove('scientific');
            this.simpleModeBtn.classList.add('active');
            this.scientificModeBtn.classList.remove('active');
        }

        // Save preference to localStorage
        this.saveModePreference();
    }

    saveModePreference() {
        try {
            localStorage.setItem('calculatorMode', this.isScientificMode ? 'scientific' : 'simple');
        } catch (e) {
            // localStorage not available
        }
    }

    loadModePreference() {
        try {
            const savedMode = localStorage.getItem('calculatorMode');
            if (savedMode) {
                this.setMode(savedMode);
            }
        } catch (e) {
            // localStorage not available
        }
    }

    handleButtonClick(e) {
        const btn = e.target;

        if (btn.dataset.number !== undefined) {
            this.inputNumber(btn.dataset.number);
        } else if (btn.dataset.operator) {
            this.inputOperator(btn.dataset.operator);
        } else if (btn.dataset.action) {
            this.handleAction(btn.dataset.action);
        }
    }

    handleKeyPress(e) {
        const key = e.key;

        // Numbers
        if (/^[0-9]$/.test(key)) {
            this.inputNumber(key);
            e.preventDefault();
        }
        // Operators
        else if (['+', '-', '*', '/', '^', '%'].includes(key)) {
            this.inputOperator(key);
            e.preventDefault();
        }
        // Decimal
        else if (key === '.') {
            this.handleAction('decimal');
            e.preventDefault();
        }
        // Enter or =
        else if (key === 'Enter' || key === '=') {
            this.handleAction('calculate');
            e.preventDefault();
        }
        // Backspace
        else if (key === 'Backspace') {
            this.handleAction('backspace');
            e.preventDefault();
        }
        // Escape for clear
        else if (key === 'Escape') {
            this.handleAction('clear');
            e.preventDefault();
        }
        // Delete for clear entry
        else if (key === 'Delete') {
            this.handleAction('clearEntry');
            e.preventDefault();
        }
        // Tab to toggle mode
        else if (key === 'Tab' && !e.shiftKey && !e.ctrlKey && !e.altKey) {
            e.preventDefault();
            this.setMode(this.isScientificMode ? 'simple' : 'scientific');
        }

        // Scientific function shortcuts (only in scientific mode)
        if (this.isScientificMode) {
            if (key === 's' && !e.ctrlKey) {
                this.handleAction('sin');
                e.preventDefault();
            }
            else if (key === 'c' && !e.ctrlKey) {
                this.handleAction('cos');
                e.preventDefault();
            }
            else if (key === 't' && !e.ctrlKey) {
                this.handleAction('tan');
                e.preventDefault();
            }
            else if (key === 'l' && !e.ctrlKey) {
                this.handleAction('log');
                e.preventDefault();
            }
            else if (key === 'n' && !e.ctrlKey) {
                this.handleAction('ln');
                e.preventDefault();
            }
            else if (key === 'r' && !e.ctrlKey) {
                this.handleAction('sqrt');
                e.preventDefault();
            }
            else if (key === '!' && !e.ctrlKey) {
                this.handleAction('fact');
                e.preventDefault();
            }
            else if (key === 'p' && !e.ctrlKey) {
                this.handleAction('pi');
                e.preventDefault();
            }
            else if (key === 'e' && !e.ctrlKey) {
                this.handleAction('e');
                e.preventDefault();
            }
        }
    }

    handleAction(action) {
        // Scientific functions that call the API
        const scientificFunctions = [
            'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
            'log', 'ln', 'exp', 'sqrt', 'sqr', 'cbrt',
            'inv', 'abs', 'neg', 'fact'
        ];

        if (scientificFunctions.includes(action)) {
            this.calculateScientific(action);
            return;
        }

        switch (action) {
            case 'clear':
                this.clear();
                break;
            case 'clearEntry':
                this.clearEntry();
                break;
            case 'backspace':
                this.backspace();
                break;
            case 'decimal':
                this.inputDecimal();
                break;
            case 'calculate':
                this.calculate();
                break;
            case 'pi':
                this.insertConstant(this.PI, 'π');
                break;
            case 'e':
                this.insertConstant(this.E, 'e');
                break;
        }
    }

    inputNumber(num) {
        if (this.waitingForOperand) {
            this.currentNumber = num;
            this.waitingForOperand = false;
        } else {
            this.currentNumber = this.currentNumber === '0' ? num : this.currentNumber + num;
        }
        this.updateDisplay();
    }

    inputDecimal() {
        if (this.waitingForOperand) {
            this.currentNumber = '0.';
            this.waitingForOperand = false;
        } else if (!this.currentNumber.includes('.')) {
            this.currentNumber += '.';
        }
        this.updateDisplay();
    }

    insertConstant(value, symbol) {
        this.currentNumber = value.toString();
        this.waitingForOperand = false;
        this.updateDisplay();

        // Show the symbol briefly in expression
        if (!this.expression) {
            this.expression = symbol;
            this.updateExpressionDisplay();
            setTimeout(() => {
                if (this.expression === symbol) {
                    this.expression = '';
                    this.updateExpressionDisplay();
                }
            }, 1000);
        }
    }

    inputOperator(op) {
        const inputValue = parseFloat(this.currentNumber);

        if (this.previousNumber === null) {
            this.previousNumber = inputValue;
        } else if (this.operator && !this.waitingForOperand) {
            // Chain calculations
            this.calculate(false);
        }

        this.operator = op;
        this.waitingForOperand = true;
        this.expression = `${this.formatDisplay(this.previousNumber)} ${this.getOperatorSymbol(op)}`;
        this.updateExpressionDisplay();
        this.highlightOperator(op);
    }

    getOperatorSymbol(op) {
        const symbols = {
            '+': '+',
            '-': '−',
            '*': '×',
            '/': '÷',
            '^': '^',
            '%': 'mod'
        };
        return symbols[op] || op;
    }

    highlightOperator(op) {
        document.querySelectorAll('.btn-operator, .btn-function[data-operator]').forEach(btn => {
            btn.classList.remove('active');
            if (btn.dataset.operator === op) {
                btn.classList.add('active');
            }
        });
    }

    clearOperatorHighlight() {
        document.querySelectorAll('.btn-operator, .btn-function').forEach(btn => {
            btn.classList.remove('active');
        });
    }

    backspace() {
        if (this.waitingForOperand) return;

        if (this.currentNumber.length > 1) {
            this.currentNumber = this.currentNumber.slice(0, -1);
            // Handle case where we might have just "-" left
            if (this.currentNumber === '-') {
                this.currentNumber = '0';
            }
        } else {
            this.currentNumber = '0';
        }
        this.updateDisplay();
    }

    clearEntry() {
        this.currentNumber = '0';
        this.updateDisplay();
    }

    clear() {
        this.currentNumber = '0';
        this.previousNumber = null;
        this.operator = null;
        this.waitingForOperand = false;
        this.expression = '';
        this.lastResult = null;
        this.updateDisplay();
        this.updateExpressionDisplay();
        this.clearOperatorHighlight();
        this.displayResult.classList.remove('error');
    }

    async calculate(updateExpression = true) {
        if (this.operator === null || this.previousNumber === null) {
            return;
        }

        const operand1 = this.previousNumber;
        const operand2 = parseFloat(this.currentNumber);

        if (updateExpression) {
            this.expression = `${this.formatDisplay(operand1)} ${this.getOperatorSymbol(this.operator)} ${this.formatDisplay(operand2)}`;
            this.updateExpressionDisplay();
        }

        try {
            const response = await this.callAPI(operand1, this.operator, operand2);

            if (response.success) {
                this.currentNumber = response.display;
                this.previousNumber = response.result;
                this.lastResult = response.result;
                this.operator = null;
                this.waitingForOperand = true;
                this.updateDisplay(true);
                this.clearOperatorHighlight();
            } else {
                this.showError(response.error);
            }
        } catch (error) {
            this.showError('Connection error');
        }
    }

    async calculateScientific(funcName) {
        const operand = parseFloat(this.currentNumber);
        const displayName = this.functionNames[funcName] || funcName;

        // Build expression display
        if (funcName === 'fact') {
            this.expression = `${this.formatDisplay(operand)}!`;
        } else if (funcName === 'abs') {
            this.expression = `|${this.formatDisplay(operand)}|`;
        } else if (funcName === 'sqr') {
            this.expression = `(${this.formatDisplay(operand)})²`;
        } else if (funcName === 'inv') {
            this.expression = `1/${this.formatDisplay(operand)}`;
        } else if (funcName === 'neg') {
            this.expression = `±(${this.formatDisplay(operand)})`;
        } else {
            this.expression = `${displayName}(${this.formatDisplay(operand)})`;
        }
        this.updateExpressionDisplay();

        try {
            const response = await this.callAPI(operand, funcName, null);

            if (response.success) {
                this.currentNumber = response.display;
                this.previousNumber = null;
                this.lastResult = response.result;
                this.operator = null;
                this.waitingForOperand = true;
                this.updateDisplay(true);
            } else {
                this.showError(response.error);
            }
        } catch (error) {
            this.showError('Connection error');
        }
    }

    async callAPI(operand1, operator, operand2) {
        const body = {
            operand1: operand1,
            operator: operator
        };

        if (operand2 !== null) {
            body.operand2 = operand2;
        }

        const response = await fetch('/api/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        });

        if (!response.ok) {
            const error = await response.json();
            return { success: false, error: error.detail?.error || 'Calculation error' };
        }

        return await response.json();
    }

    showError(message) {
        this.displayResult.textContent = message;
        this.displayResult.classList.add('error', 'shake');

        setTimeout(() => {
            this.displayResult.classList.remove('shake');
        }, 500);

        setTimeout(() => {
            this.clear();
        }, 2000);
    }

    formatDisplay(num) {
        if (num === null) return '';

        // Handle very large or small numbers
        const absNum = Math.abs(num);
        if (absNum >= 1e10 || (absNum < 1e-6 && absNum > 0)) {
            return num.toExponential(6);
        }

        // Remove trailing zeros
        return parseFloat(num.toPrecision(10)).toString();
    }

    updateDisplay(animate = false) {
        let display = this.currentNumber;

        // Handle long numbers
        if (display.length > 14) {
            const num = parseFloat(display);
            display = num.toExponential(8);
        }

        this.displayResult.textContent = display;
        this.displayResult.classList.remove('error');

        if (animate) {
            this.displayResult.classList.add('updated');
            setTimeout(() => {
                this.displayResult.classList.remove('updated');
            }, 200);
        }
    }

    updateExpressionDisplay() {
        this.displayExpression.textContent = this.expression;
    }
}

// Initialize calculator when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new Calculator();
});
