pkgname=raad
pkgver=0.1.0
pkgrel=1
pkgdesc="Simple CLI tool that runs sudo -u <user> commands with a remembered target"
arch=('any')
url="https://github.com/at-elcapitan/raad"
license=('MIT')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-setuptools')
source=("$pkgname-$pkgver.tar.gz")
sha256sums=('SKIP')

build() {
  cd "$srcdir"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
