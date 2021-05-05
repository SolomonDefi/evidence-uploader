class UidSingleton {
  constructor() {
    this._counter = 0;
  }

  next() {
    this._counter += 1;
    return this._counter;
  }
}

const uidSingleton = new UidSingleton();

const useUid = () => (
  uidSingleton.next()
);

export default useUid;
