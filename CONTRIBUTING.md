# Contributing to Steins Gate

Thank you for your interest in contributing to Steins Gate! This document provides guidelines and information for contributors.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Install dependencies: `pip install -r requirements.txt`
4. Create a new branch for your feature: `git checkout -b feature/your-feature`

## Development Setup

### Local Environment
```bash
# Clone the repository
git clone https://github.com/owaiskaifi/steins-gate.git
cd steins-gate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Testing Your Changes
- Test the API endpoint with the provided `send.py` script
- Ensure the web interface loads correctly
- Verify that your changes don't break existing functionality

## Code Guidelines

### Python Code Style
- Follow PEP 8 conventions
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and single-purpose

### API Changes
- Maintain backward compatibility when possible
- Update documentation for any API changes
- Test edge cases and error conditions

## Submitting Changes

1. **Create a Pull Request**
   - Provide a clear title and description
   - Reference any related issues
   - Include screenshots for UI changes

2. **Pull Request Checklist**
   - [ ] Code follows project conventions
   - [ ] Tests pass (if applicable)
   - [ ] Documentation updated
   - [ ] No breaking changes (or clearly documented)

## Types of Contributions

### Bug Fixes
- Report bugs with clear reproduction steps
- Include error messages and stack traces
- Test your fix thoroughly

### New Features
- Discuss major changes in issues first
- Ensure features align with project goals
- Update documentation and examples

### Documentation
- Fix typos and unclear explanations
- Add missing documentation
- Improve code examples

## Model Updates

If contributing changes to the machine learning model:

1. Document the training process
2. Include model performance metrics
3. Ensure backward compatibility with existing API
4. Update the `model.pkl` file appropriately

## Questions?

- Open an issue for questions about the codebase
- Check existing issues before creating new ones
- Be respectful and constructive in discussions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.