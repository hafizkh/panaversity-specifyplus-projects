/**
 * Calculator Web UI Application
 * Modern/Minimal calculator with API backend
 */

class Calculator {
    constructor() {
        this.currentNumber = '0';
        this.previousNumber = null;
        this.operator = null;
        this.waitingForOperand = false;
        this.expression = '';

        this.displayResult = document.getElementById('result');
        this.displayExpression = document.getElementById('expression');

        this.init();
    }

    init() {
        // Button click handlers
        document.querySelectorAll('.btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.handleButtonClick(e));
        });

        // Keyboard support
        document.addEventListener('keydown', (e) => this.handleKeyPress(e));
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
            this.backspace();
            e.preventDefault();
        }
        // Escape or c/C for clear
        else if (key === 'Escape' || key.toLowerCase() === 'c') {
            this.handleAction('clear');
            e.preventDefault();
        }
    }

    handleAction(action) {
        switch (action) {
            case 'clear':
                this.clear();
                break;
            case 'decimal':
                this.inputDecimal();
                break;
            case 'calculate':
                this.calculate();
                break;
            case 'sqrt':
                this.calculateSqrt();
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
            '%': '%'
        };
        return symbols[op] || op;
    }

    highlightOperator(op) {
        document.querySelectorAll('.btn-operator').forEach(btn => {
            btn.classList.remove('active');
            if (btn.dataset.operator === op) {
                btn.classList.add('active');
            }
        });
    }

    clearOperatorHighlight() {
        document.querySelectorAll('.btn-operator').forEach(btn => {
            btn.classList.remove('active');
        });
    }

    backspace() {
        if (this.waitingForOperand) return;

        if (this.currentNumber.length > 1) {
            this.currentNumber = this.currentNumber.slice(0, -1);
        } else {
            this.currentNumber = '0';
        }
        this.updateDisplay();
    }

    clear() {
        this.currentNumber = '0';
        this.previousNumber = null;
        this.operator = null;
        this.waitingForOperand = false;
        this.expression = '';
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

    async calculateSqrt() {
        const operand = parseFloat(this.currentNumber);
        this.expression = `√${this.formatDisplay(operand)}`;
        this.updateExpressionDisplay();

        try {
            const response = await this.callAPI(operand, 'sqrt', null);

            if (response.success) {
                this.currentNumber = response.display;
                this.previousNumber = null;
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
        const display = this.currentNumber.length > 12
            ? parseFloat(this.currentNumber).toExponential(6)
            : this.currentNumber;

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
